import os
from os.path import isfile, join


class FindBiggestFile():
    def __init__(self):
        self.path = os.getcwd()
        self.files = []
        self.bigger_size = 0
        self.bigger_file = None

    def get_files(self):
        for item in os.listdir(self.path):
            path_to_item = join(self.path, item)
            if isfile(path_to_item):
                self.files.append(path_to_item)
            else:
                self.files.extend(get_files(path_to_item))
        return self.files

    def find_file(self):
        self.files = self.get_files()
        for file_str in self.files:
            st = os.stat(file_str)
            if st.st_size > self.bigger_size:
                self.bigger_size = st.st_size
                self.bigger_file = file_str
        print('Answer {0}'.format(self.bigger_file))


def main():
    fbf = FindBiggestFile()
    fbf.get_files()
    fbf.find_file()


if __name__ == "__main__":
    main()