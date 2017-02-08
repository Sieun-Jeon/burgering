from burgering.datatypes import Integer
from burgering import Patty

name = 'plus3'
color = '#553355'
author = 'cookieshake'

title = {'default': 'Plus3'}
description = {'default': 'Adds 3 to the input',
               'ko': '입력 값에 3을 더합니다'}

input_type = Integer
output_type = Integer

dependencies = []
properties_format = {}


class Plus3Patty(Patty):
    def burn(self, input_data, properties):
        int_input = input_data.get()

        i = Integer()
        i.set(int_input + 3)

        return i

patty = Plus3Patty

