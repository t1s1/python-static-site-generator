from pathlib import Path
from typing import List


class Parser:
    extensions = List[str]

    def valid_extension(self, extension):
        return extension in self.expressions

    def parse(List[path], List[source], List[dest]):
        raise NotImplementedError()

    def read(path):
        with open(path, mode="r") as file:
            return file.read()

    def write(path, dest, content):
        ext = ".html"
        full_path = self.dest

        full_path = full_path + dest / path.with_suffix(ext).name






