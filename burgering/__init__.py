from importlib import import_module
from burgering.exceptions import WrongResult
patties_direction = "../patties"

class Patty:
    name = 'patty'
    burger = None
    type = ''
    title = {'default': ''}
    description = {}
    author = 'NULL'

    properties = {}
    input_data = None
    output_data = None

    def burn(self, input_data):
        pass

    def run(self):
        self.output_data = self.burn(self.input_data, self.properties)


class Burger:
    def __init__(self):
        self.recipe = []
        self.properties_list = []
        self.status = []

    def check_patty(self,patty_name):#Patties 폴더에 patty_name 있는지 검색
        import os
        patties_list = os.listdir(patties_direction)
        for each in patties_list:
            if patty_name == each.split('.')[0]:
                return True
        return False

    def add_patty(self, patty_name, index):
        self.recipe.insert(index, patty_name)
        self.properties_list.insert(index, {})
        self.status = self.status[:index]

        if self.check_patty(patty_name):
            #Todo add patty
        else:
            rslt = self.communicate(None,"패티가 존재하지 않습니다. 패티 마트로 이동할까요?",["Yes","No"])
            if rslt == "Yes":
                #TODO 패티마트
            elif rslt =="No":
                self.communicate(None,"다른 패티를 추가해주세요",[])
            else:
                raise WrongResult("burgering")

            self.buy_patty(patty_name)
        self.run()

    def buy_patty(self,patty_name):
        #패티 다운로드

    def del_patty(self, index):
        self.recipe.pop(index)
        self.properties_list.pop(index)
        self.status = self.status[:index]

        self.run()
    def communicate(self,patty,contents,results):
        #patty = 요청한 패티, Contents는 유저에게 보여줄 내용, results는 유저가 고를 수 있는 result의 모임
        #TODO user에게 contents전달하고 result 받음(GUI상)
        result = "TEST"
        return result

    def set_property(self, index, property):
        self.properties_list[index] = property

        self.run()

    def run(self):
        for i in range(len(self.recipe)):
            if i < len(self.status):
                continue

            current_patty_name = self.recipe[i]
            current_module = import_module('patties.' + current_patty_name)

            if i == 0:
                if current_module.input_type is not None:
                    break
            else:
                prev_patty_name = self.recipe[i-1]
                prev_module = import_module('patties.' + prev_patty_name)

                if not prev_module.output_type == current_module.input_type:
                    break

            if not len(self.properties_list[i]) == len(current_module.properties_format):
                break

            patty = current_module.patty()
            patty.input_data = self.status[i-1] if i is not 0 else None
            patty.properties = self.properties_list[i]
            patty.run()

            self.status.append(patty.output_data)

if __name__ == '__main__':
    b = Burger()

    def add_patty(patty_name, index, property={}):
        print("Add Patty '{}'".format(patty_name))
        b.add_patty(patty_name, index)
        b.set_property(index, property)
        print('Recipe: ' + str(b.recipe))
        print('Status: ' + str(b.status))
        print()

    def del_patty(index):
        pass

    add_patty('readint', 0, {'int': 0})
    add_patty('plus3', 1)
    add_patty('plus3', 2)
    add_patty('printint', 3)






