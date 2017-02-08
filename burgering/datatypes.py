import pickle


class Model:
    prefix = 'm'


class Data:
    _data = None
    _file = None

    prefix = 'd'

    def save(self, path):
        pickle.dump(self._data, open(path, "wb"))

    def load(self, path):
        self._data = pickle.load(open(path, "rb" ))


class ProcessedData:
    prefix = 'pd'


class TrainingData:
    prefix = 'dt'


class ValidatingData:
    prefix = 'dv'


class Graph:
    prefix = 'g'
