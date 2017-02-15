from burgering.datatypes import Data
from burgering.exceptions import FileTypeMismatched
from burgering import Patty
import pandas as pd


class LoadFile(Patty):
    name = 'loadFile'
    type = 'm'
    title = {'default': 'Load File'}
    description = {'en': 'Load file(csv,txt,json)',
                   'ko': 'csv,txt,json 형태의 파일을 불러옵니다.'}

    author = 'sieunj'

    input_type = None
    output_type = Data

    dependencies = ['pandas']
    properties_format = {'delim': str}

    def burn(self):
        filename="hello.csv"  #Todo change
        '''
        extension = filename.split(".")[len(filename.split("."))-1]
        data = Data()

        if extension == 'txt' or extension == 'csv':
            data = pd.read_csv(filename, sep=self.properties['delim'])
        elif extension =='json':
            data = pd.read_json(filename)
        else:
            raise FileTypeMismatched() #TODO change
        '''
        return Data()


patty = LoadFile

