
from datetime import datetime

def readFile(name):
    list = []
    with open(name+".txt") as f:
        lines = f.readlines()
    for line in lines:
        list.append(line.strip())
    return list

def userToDicc(line):

    userLine=line.split("=")
    key=userLine[0]
    listSchedule = userLine[1].split(",")
    value = scheduleToDicc(listSchedule)

    return key,value

def scheduleToDicc(list):
    dicc={}
    for s in list:
        key = s[:2]
        value = s[2:]
        value=tuple(value.split("-"))
        dicc[key]=value
    return dicc

def fileToDicc(name):
    lines=readFile(name)
    dicc={}
    for line in lines:
        key,value = userToDicc(line)
        dicc[key] = value
    return dicc

def compareUsers(dicc):
    comparation=[]
    keys = dicc.keys()
    key_list = list(keys)
    for i in range(len(key_list)):
        for j in range(i+1,len(key_list)):
            dicc1 = dicc[key_list[i]]
            dicc2 = dicc[key_list[j]]
            times = compareDicc(dicc1,dicc2)
            if times>0:
                comparation.append((key_list[i],key_list[j],str(times)))
    return comparation

def compareHours(hours1,hours2):
    h1_a = datetime.strptime(hours1[0], '%H:%M').time()
    h1_b = datetime.strptime(hours1[1], '%H:%M').time()
    h2_a = datetime.strptime(hours2[0], '%H:%M').time()
    h2_b = datetime.strptime(hours2[1], '%H:%M').time()
    if h1_a >= h2_a and h1_a <= h2_b:
        return True
    elif h1_b >= h2_a and h1_b <= h2_b:
        return True
    elif h2_a >= h1_b and h2_a <= h1_b:
        return True
    elif h2_b >= h1_a and h2_b <= h1_b:
        return True
    else:
        return False

def compareDicc(dicc1,dicc2):
    c=0
    for key in dicc1:
        if key in dicc2:
            if compareHours(dicc1[key],dicc2[key]):
                c+=1
    return c

def formatResults(results):
    for result in results:
        name1 = result[0]
        name2 = result[1]
        times = result[2]
        print(name1+"-"+name2+":"+times)

def runProgram():
    employees_dicc = fileToDicc("file")
    results = compareUsers(employees_dicc)
    formatResults(results)

runProgram()