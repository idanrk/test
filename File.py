import sys


class File:
    def __init__(self, filename="file.txt"):
        with open(filename) as f:  # sys.argv[1]
            self.content = f.read()

    def get_content(self):
        return self.content
