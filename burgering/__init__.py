from importlib import import_module
from burgering.exceptions import WrongResult, PattyNotExists

patties_direction = "../patties"


class Patty:
    burger = None

    name = 'patty'
    type = ''
    title = {'default': ''}
    description = {}
    author = 'NULL'

    properties = {}
    input_type = None
    output_type = None

    input_data = None
    output_data = None

    def burn(self):
        pass

    def run(self):
        # properties에 빈 칸(None)이 있는지 검사
        for k, v in self.properties.items():
            if v is None:
                return None

        # input type이 존재할 때 input data와 type이 맞는지 검사
        if self.input_type is not None:
            if len(self.input_type) is not len(self.input_data):
                self.alert('적절한 input값이 없어 패티를 구울 수 없습니다', ['OK'])
                return None
            if False in map(lambda x: isinstance(x[1], x[0]), zip(self.input_type, self.input_data)):
                return None

        # 모든 조건이 맞으면 패티 굽기
        result = self.burn(*self.input_data)
        if isinstance(result, tuple):
            self.output_data = result
        else:
            self.output_data = (result,)

    def alert(self, contents, results):
        self.burger.alert(self, contents, results)


class Burger:
    def __init__(self):
        self.recipe = []

    def check_patty(self,patty_name):  # Patties 폴더에 patty_name 있는지 검색
        import os
        patties_list = os.listdir(patties_direction)
        for each in patties_list:
            if patty_name == each.split('.')[0]:
                return True
        return False

    def add_patty(self, patty_name, index):
        # 패티가 존재하는지 확인하고, 문제 시 사용자에게 해결방법 질문
        if self.check_patty(patty_name):
            pass
        else:
            rslt = self.alert(None, "패티가 존재하지 않습니다. 패티 마트로 이동할까요?", ["Yes", "No"])
            if rslt == "Yes":
                # TODO 패티마트
                pass
            elif rslt == "No":
                self.alert(None, "다른 패티를 추가해주세요", ['Ok'])
                return None

            self.buy_patty(patty_name)

        # patty가 담긴 module을 동적으로 import해서 추가
        patty_module = import_module('patties.' + patty_name)
        p = patty_module.patty()
        p.burger = self
        self.recipe.append(p)

        # 추가된 패티 뒤의 패티들의 data 초기화
        for p in self.recipe[index:]:
            p.input_data = None
            p.output_data = None

        self.run()

    def buy_patty(self,patty_name):
        #패티 다운로드
        pass

    def del_patty(self, index):
        self.recipe.pop(index)

        # 삭제된 patty 뒤의 패티들의 data 초기화
        for p in self.recipe:
            p.input_data = None
            p.output_data = None

        self.run()

    def alert(self, patty, contents, results):
        # patty = 요청한 패티, Contents는 유저에게 보여줄 내용, results는 유저가 고를 수 있는 result의 모임
        # TODO user에게 contents전달하고 result 받음(GUI상)
        # 디버그 용도로 input을 통해 사용자와 상호작용 할 수 있도록 함
        result = input('({}) {} {}: '.format(patty.title['default'] if patty is not None else 'Global'
                                             , contents, str(results)))

        if result not in results:
            raise WrongResult()

        return result

    def run(self):
        for index in range(len(self.recipe)):
            patty = self.recipe[index]

            if patty.input_type is None:  # patty의 input type이 없을 때
                pass
            else:  # patty의 input type이 존재할 때
                outputs = reversed([output for output in [p.output_data for p in self.recipe[:index]]]) #  지금까지 나온 output들의 list 역순
                patty_input = []

                for i in patty.input_type:
                    for o in outputs:
                        if type(o) is i:
                            patty_input.append(o)
                            break  # input type 하나를 찾았으면 for o in outputs 를 끝냄

                patty.input_data = tuple(patty_input)

            patty.run()


if __name__ == '__main__':
    b = Burger()

    def add_patty(patty_name, index, property={}):
        print("Add Patty '{}'".format(patty_name))
        b.add_patty(patty_name, index)
        print('Recipe: ' + str(b.recipe))

    def del_patty(index):
        pass

    add_patty('Preprocessing', 0)
    pass







