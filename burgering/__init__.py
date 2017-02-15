from importlib import import_module

import os
import random


class Patty:
    name = ''
    author = ''

    title = {'en': ''}
    description = {'en': '',
                   'ko': ''}

    input_type = ()
    output_type = ()

    dependencies = []
    properties_format = {}

    properties = {}
    input_data = None
    output_data = None

    def burn(self, *input_data):
        pass

    def run(self):
        if self.input_type is None:
            self.output_data = (self.burn(),)
        else:
            self.output_data = self.burn(*self.input_data)


class Burger:
    def __init__(self):
        self.recipe = []
        self.properties_list = []
        self.status = []
        self.path = '/tmp'

    def add_patty(self, patty_name, index):
        self.recipe.insert(index, patty_name)
        self.properties_list.insert(index, {})
        self.status = self.status[:index] + [None for i in range(len(self.recipe)-index)]

        self.run()

    def del_patty(self, index):
        self.recipe.pop(index)
        self.properties_list.pop(index)
        self.status = self.status[:index] + [None for i in range(len(self.recipe)-index)]

        self.run()

    def set_property(self, properties, index):
        self.properties_list[index] = properties

        self.run()

    def run(self):
        for i in range(len(self.recipe)):

            current_patty_name = self.recipe[i]
            current_module = import_module('patties.' + current_patty_name)

            patty = current_module.patty()

            if patty.input_type is None:
                patty.input_data = None
            else:  # patty.input_type이 존재한다면
                input_types = patty.input_type if type(patty.input_type) is tuple else (patty.input_type,)  # input_type이 tuple아닐경우 tuple로 변경
                inputs = []
                outputs = [out for out in [outs for outs in self.status]]

                for i_type in input_types:
                    for output in reversed(outputs):
                        if output[:output.find('_')] == i_type.prefix:
                            patty.input_data = output
                            inputs.append()
                            break

                if len(inputs) != len(input_types):
                    continue
                if tuple(map(lambda x: type(x), inputs)) != input_types:
                    continue

            if not len(self.properties_list[i]) == len(patty.properties_format):
                return
            patty.properties = self.properties_list[i]
            patty.run()

            stat = []
            for output in patty.output_data:
                filename = '{}_{}'.format(output.prefix, self._get_id())
                output.save(os.path.join(self.path, filename))

                stat.append(filename)

            self.status[i] = tuple(stat)

    def _get_id(self):
        return str(random.randint(0, 10000))








