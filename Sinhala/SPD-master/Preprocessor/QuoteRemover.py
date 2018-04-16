class QuoteRemover:

    @staticmethod
    def remove_quotes(text):
        start = text.find("\"")
        while start != -1:
            if start != -1:
                end = text.find("\"", start + 1)
                if end != -1:
                    text = text[:start] + text[end + 1:]
                else:
                    break
            else:
                break
            start = text.find("\"")
        return text
