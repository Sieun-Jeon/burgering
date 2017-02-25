

class DataType:
    pass


class Model(DataType):
    _content = None

    def get(self):
        return self._content

    def set(self, content):
        self._content = content


class Data(DataType):
    _content = None

    def get(self):
        return self._content

    def set(self, content):
        self._content = content


class PreprocessedData(DataType):
    _content = None

    def get(self):
        return self._content

    def set(self, content):
        self._content = content


class TrainingData(DataType):
    _content = None

    def get(self):
        return self._content

    def set(self, content):
        self._content = content


class ValidationData(DataType):
    _content = None

    def get(self):
        return self._content

    def set(self, content):
        self._content = content


class Graph(DataType):
    _content = None

    def get(self):
        return self._content

    def set(self, content):
        self._content = content




