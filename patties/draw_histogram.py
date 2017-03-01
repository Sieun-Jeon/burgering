from burgering import Patty
from burgering.datatypes import Data, Graph


class DrawHistogram(Patty):
    name = 'draw_histogram'
    type = 'm'
    title = {'default': 'Histogram'}
    description = {'en': 'Draw a histogram with data',
                   'ko': '주어진 데이터를 바탕으로 히스토그램을 그립니다'}

    author = 'cookieshake'
    input_type = (Data,)
    output_type = (Graph,)

    dependencies = ['matplotlib']
    properties_format = {
        'row_to_draw': str,
        'save_path': str,
        'title': str,
        'x_label': str,
        'y_label': str
    }

    def burn(self, data):
        import matplotlib.pyplot as plt

        plt.hist(data[self.properties['row_to_draw']])
        plt.title(self.properties['title'])
        plt.xlabel(self.properties['x_label'])
        plt.ylabel(self.properties['y_label'])

        plt.savefig(self.properties['save_path'])

        return Graph()




