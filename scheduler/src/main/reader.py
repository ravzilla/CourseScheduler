'''
Created on Nov 3, 2015

@author: Ravi
'''


def read_file(name:str)->list:
    f = open(name,'r')
    data = f.readlines()
    f.close()
    return data
    
def return_class(school:str,code:str,name:str)->int:
    wF = read_file(name)
    for lineNum,data in enumerate(wF):
        l= data.split()
        
        if len(l)!=0:
           if l[0] == school and l[1]==code:
               print(parse_class(lineNum,wF))
               break
def parse_class(lineNum:int,data:list)->list: 
    """times = []
    days = []
    code = 0"""
    classTypes = []    
    for n,d in enumerate(data[lineNum:]):
        
        l = d.split()
       
        if len(l)!=0:
            if 'cCode' != l[0]!='~' :
                print(l)
                if  l[1] not in classTypes:
                    classTypes.append(l[1])
    return classTypes