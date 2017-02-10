class Integer:
    _data = None

    def get(self):
        return self._data

    def set(self, integer):
        if not type(integer) == int:
            raise Exception('Input Mismatch')

        self._data = integer


class Data:
    #TODO change
    def get(self):
        return self._data

    def set(self, integer):
        if not type(integer) == int:
            raise Exception('Input Mismatch')


