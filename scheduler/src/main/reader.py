'''
Created on Nov 3, 2015

@author: Ravi
'''


def read_file(name:str)->list:
    f = open(name,'r')
    data = f.readlines()
    f.close()
    return data
    
def return_class(school:str,code:str,name:str)->list:
    wF = read_file(name)
    for lineNum,data in enumerate(wF):
        l= data.split()
        
        if len(l)!=0:
           if l[0] == school and l[1]==code:
               return parse_class(lineNum,wF)
               break
def parse_class(lineNum:int,data:list)->list: 
    
    classes =[]
    for n,d in enumerate(data[lineNum+1:]):
        
        l = d.split()
       
        if len(l)!=0:
               
            if l[0] != 'CCode' and l[0] != '~':
              classes.append([int(l[0]),l[1],(l[5])])
              
        else:
            break
    return classes
def parse_day(s:str)->list:
    result = [False]*5
    t= ['M','Tu','W','Th','F']
    for i in range(0,len(t)):
        if t[i] in s:
            result[i] = True
    return result
