from Test.readDocuments import ReadDocuments

if __name__ == '__main__':

    md = ReadDocuments()
    docList = md.readDocuments()
    print(docList)

    compareDocs = SPD()
    output = compareDocs.compare(docList)