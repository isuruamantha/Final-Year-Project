import requests


class SynonymReplacer:

    @staticmethod
    def replace_synonyms(tokens_list):
        new_list = []
        for token in tokens_list:
            try:
                response = requests.get("http://localhost:8080/Ajax/" + token + "/synonyms")
                synonyms = response.json()
                if synonyms is not None and len(synonyms) > 0:
                    print(synonyms)
                    new_list.append(synonyms[0].strip())
                else:
                    new_list.append(token)
            except Exception as e:
                print("Error occurred when finding synonyms for %s -> %s" % (token, e))
                new_list.append(token)

        return new_list
