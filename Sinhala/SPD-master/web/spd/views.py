from time import timezone

from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.utils.encoding import smart_text

from detector.SPD import SPD
from .models import Doc


def index(request):
    template = loader.get_template("spd/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def compare(request):
    doc = request.FILES.get('doc')
    text = smart_text(doc.read())
    std_text = SPD.standardize(text)

    template = loader.get_template("spd/index.html")

    try:
        docs = Doc.objects.all().filter(name=doc.name).get()
        print("Found same doc - %s" % docs)
        context = {
            'error': 'The same document is available in our database. Please upload another.'
        }
        return HttpResponse(template.render(context, request))
    except Exception as a:
        print(a)

    try:
        docs = Doc.objects.all().values('name', 'standardized_content')
        docs = list(docs)
    except Exception as e:
        print(e)
        docs = []

    print("Available docs are - %s" % docs)

    # Add the new one now
    d = Doc(name=doc.name, content=text, standardized_content=std_text, created_at=timezone.now())
    d.save()
    print("Doc added - %s" % doc.name)
    docs.append({
        'name': doc.name,
        'standardized_content': std_text
    })

    similarities = SPD.compare(docs)
    return HttpResponse(template.render(similarities, request))


def upload_multiple_docs(request):
    files = request.FILES.getlist('file')
    documents = []
    for f in files:
        print(f)
        read_file = f.read().decode("utf-8")
        documents.append({
            'name': f.name,
            'text': SPD.standardize(read_file)
        })

    template = loader.get_template("spd/index.html")
    uniqueness, docs = SPD.compare_uploaded_files(documents)
    context = {
        'results': uniqueness,
        'docs': docs
    }
    return HttpResponse(template.render(context, request))
