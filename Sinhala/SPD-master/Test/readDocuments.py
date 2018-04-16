import os
import glob

class ReadDocuments:

    def readDocuments (self):
        docs = []
        path = '/home/erandi/PycharmProjects/SPD/Test'
        for infile in glob.glob(os.path.join(path, '*.txt')):
            docs.append(infile)
            print("current file is: " + infile)

        return docs