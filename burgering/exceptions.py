class InputMismatch(Exception):
    def __init__(self):
        super(InputMismatch, self).__init__()


class FileTypeMismatched(Exception):
    def __init__(self):
        print("ERROR : File type mismatched!") #todo change

class paramMismatch(Exception):
    def __init__(self):
        print("ERROR : param mismatched!") #todo change

class WrongResult(Exception):
    def __init__(self,pattyname,err):
        print("ERROR ["+pattyname+"] : result error!") #todo change

class PattyNotExists(Exception):
    def __init__(self):
        super(PattyNotExists, self).__init__('Patty not exists!')