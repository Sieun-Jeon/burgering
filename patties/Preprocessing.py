from burgering.datatypes import Data
from burgering.exceptions import  paramMismatch, WrongResult
from burgering import Burger, Patty
from burgering.datatypes import *
import pandas as pd

class Preprocessing(Patty):
    name ='preprocessing'
    type = 'm'
    title = {'default': 'Preprocessing'}
    description = {'en': 'Check shape and type of the data, select columns and rows and remove outliers',
                   'ko': '데이터 형태를 확인하고 일부 데이터를 선택하거나 이상치를 제거할 수 있습니다'}

    author = 'ginger_ale'
    input_type = 'Data' #TODO change
    output_type = 'Data' #Todo change

    dependencies = []
    properties_format = {}
    data = pd.DataFrame



    def shape(self,data):
        return data.shape

    #Return list of colname and row number whose value is null
    def check_null(self,data):
        header = list(data)
        null_list = []
        for colname in header:
            for i in range(0,len(data[colname])):
                if pd.isnull(data[colname][i]):
                    null_list.append([colname,i])
        self.manage(self,data,null_list)
        return null_list

    def check_outlier(self,data,col):
        q3=data[col].quantile(0.75)
        q1=data[col].quantile(0.25)
        outlier_list = []
        for i in range(0, len(data[col])):
            x = data[col][i]
            if x < q1-(q3-q1)*1.5 or x > q3+(q3-q1)*1.5:
                outlier_list.append([col,i])
        self.manage(self,data,outlier_list)
        return outlier_list


    def manage(self,data,list):
        rslt = Burger.communicate(self.burger,self,"이상값이 총 "+len(list)+"개 입니다.",["전부 삭제","개별 확인","변경하지 않음"])
        if rslt == "전부 삭제":
            result_list = ['행 삭제', '열 삭제', '변경하지 않음']
            mssg = "전체 outlier에 대해 할 행동을 골라주세요"
            result = Burger.communicate(self.burger, self, mssg, result_list)
            if result == '행 삭제':
                col =[]
                for each in list:
                    if each[0] not in col:
                        col.append(each[0])
                self.data = self.remove(self,data,col,'c')
                mssg = str(col) + " : 삭제되었습니다."
                Burger.communicate(self.burger,self,mssg,[])
            elif result =="열 삭제":
                row = []
                for each in list:
                    if each[1] not in row:
                        row.append(each[1])
                self.data = self.remove(self,data,row,'r')
                mssg = str(row) + " : 삭제되었습니다."
                Burger.communicate(self.burger,self,mssg,[])

            else:
                raise WrongResult(self,result)

        elif rslt == '개별 확인':
            count = 1
            for each in list:
                result_list = ['행 삭제','열 삭제','값 변경','변경하지 않음']
                mssg = "이상값(%d/%d) : 행 - %s     열 - %d", count,len(list),each[0], each[1]
                result = Burger.communicate(self.burger,self,mssg,result_list)
                if result == '행 삭제':
                    self.data = self.remove(self,self.data,each[0],'c')
                elif result == '열 삭제':
                    self.data = self.remove(self, self.data, each[1], 'r')
                elif result =='값 변경':
                    rslt = Burger.communicate(self.burger,self,"수정할 값을 입력하세요")

                    Burger.communicate(self.burger,self,"변경할 값을 입력해주세요 : ", )

                else:
                    raise WrongResult(self,result)
                count += 1
        elif rslt == '변경하지 않음':
            0
        else:
            raise WrongResult(self,rslt)




    def remove(self,data,id,flag): #flag = 'r' or 'c'
        if (flag == 'c'):
            return data.drop(id,axis=1)
        elif (flag =='r'):
            return data.drop(id,axis=0)
        else:
            raise paramMismatch

    def select_col(self,data,id_list,axis):


    def burn(self,input_data):
        self.data = input_data

        #이걸 sequencial하게 하는게 아니라 유저가 선택해야 하는거 아닌가...?
        self.check_null(self.data)
        self.check_outlier(self.data)

        return self.data


patty = Preprocessing

