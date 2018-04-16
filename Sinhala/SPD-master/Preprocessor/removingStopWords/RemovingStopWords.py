import io
import Preprocessor


class RemovingStopWords:
    def removeStopwords(self, tokens_list):
        path = Preprocessor.__file__
        path = path.replace("__init__.py", "resources/stopWordList.txt")
        fin = io.open(path, "r", encoding='utf-8').read().replace('\n', ' ')
        return [token for token in tokens_list if token not in fin]
