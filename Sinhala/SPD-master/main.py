import io

from Preprocessor.QuoteRemover import QuoteRemover

txt = io.open("f.txt").read()
print(txt)
txt = QuoteRemover.remove_quotes(txt)
print(txt)
