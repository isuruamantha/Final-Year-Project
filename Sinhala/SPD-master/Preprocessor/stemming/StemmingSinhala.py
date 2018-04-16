import io

import Preprocessor


class StemmingSinhala():
    def stem(self, tokens_list):
        path = Preprocessor.__file__
        path = path.replace("__init__.py", "resources/suffixes.txt")

        try:
            suffix_list = io.open(path, "r", encoding='utf-8').read().splitlines()
        except UnicodeDecodeError:
            suffix_list = io.open(path, "r", encoding='latin-1').read().splitlines()

        stemmed = []
        for token in tokens_list:
            word = token
            for suffix in suffix_list:
                if word.endswith(suffix):
                    word = word.replace(suffix, "")
            stemmed.append(word)

        return stemmed
