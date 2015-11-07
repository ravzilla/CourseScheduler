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
            print(l)
            if l[0] == school and l[1]==code:
               return parse_class(lineNum,wF)
               break
          
def parse_class(lineNum:int,data:list)->list: 
    
    classes =[]
    for n,d in enumerate(data[lineNum+1:]):
        
        l = d.split()
     
        if len(l)!=0:
               
            if l[0] != 'CCode' and l[0] != '~':
                if l[6] != '*TBA*' :
                    classes.append([int(l[0]),l[1],(l[5]),True if l[-1] == 'OPEN' else False,parse_time([l[6],l[7]])])
              
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
    
def parse_time(comb:list):
    s=''
    if comb[0][-1] =='-':
        s=comb[0]+comb[1]
    else:
        s=comb[0]
    ampmChange = False
    pm = False
    if s[-1] == 'p':
        pm = True
        s=s[:-1]
 
    time = []
    for i,v in enumerate(s.split('-')[0].split(':')+s.split('-')[1].split(':')):
        time.append(int(v))
    if pm:
        if time[0] == 12 and time[2] < 12:
            ampmChange = True
    if pm:
        if not ampmChange:
            time[0] += 12
        time[2] += 12
    
    pm = False
   
    return time