from burgering import Patty
from burgering.datatypes import Data, Graph

from bokeh.charts import Histogram, output_file, save
from bokeh.sampledata.autompg import autompg


class DrawHistogram(Patty):
    name = 'draw_histogram'
    type = 'm'
    title = {'default': 'Histogram'}
    description = {'en': 'Draw a histogram with data',
                   'ko': '주어진 데이터를 바탕으로 히스토그램을 그립니다'}

    author = 'cookieshake'
    input_type = (Data,)
    output_type = (Graph,)

    dependencies = ['bokeh']
    properties_format = {'row_to_draw': str, 'save_path': str}

    def burn(self, data):

        self.properties = {'row_to_draw': 'mpg', 'save_path': 'test.html'}

        p = Histogram(autompg[self.properties['row_to_draw']])
        output_file(self.properties['save_path'])
        save(p)
