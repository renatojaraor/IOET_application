'''
This is an exercise for an application to IOET

Developed by: Renato Jara
'''

# imports
from datetime import datetime


def readFile(name):
    '''
    INPUT: The name of the file as string (without extension)
    OUTPUT: A list with it's lines.

    Example:
    INPUT: "file"
    OUTPUT: ["line1","line2","line3",...]
    '''
    text_lines = []
    with open(name+".txt") as f:
        lines = f.readlines()
    for line in lines:
        text_lines.append(line.strip())
    #print(text_lines)
    return text_lines

def userToDicc(line):
    '''
    INPUT: A string with a employee's schedule format
    OUTPUT: 2 values: 1st -> The user's name
                      2nd -> A list with the employee's schedule

    Example:
    INPUT: "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
    OUTPUT: "ASTRID", ["MO10:00-12:00","TH12:00-14:00","SU20:00-21:00"]
    '''

    userLine=line.split("=")
    key=userLine[0]
    listSchedule = userLine[1].split(",")
    value = scheduleToDicc(listSchedule)
    #print(key,value)
    return key,value

def scheduleToDicc(schedule):
    '''
    INPUT: A list with the employee's schedule
    OUTPUT: A dicctionary with the days as key and the hours as a tuple

    Example:
    INPUT: ["MO10:00-12:00","TH12:00-14:00","SU20:00-21:00"]
    OUTPUT: {"MO":("10:00","12:00"),"TH":("12:00","14:00"),"SU":("20:00","21:00")}
    '''

    dicc={}
    for s in schedule:
        key = s[:2]
        value = s[2:]
        value=tuple(value.split("-"))
        dicc[key]=value
    #print(dicc)
    return dicc

def fileToDicc(name):
    '''
    INPUT: The name of the file as string (without extension)
    OUTPUT: A dictionary with the employee's name as key and the employee's schedule dictionary as value

    Example:
    INPUT:"file"
    OUTPUT: {'RENE': {'MO': ('10:00', '12:00'), 'TU': ('10:00', '12:00'), 'TH': ('01:00', '03:00'), 'SA': ('14:00', '18:00'), 'SU': ('20:00', '21:00')}, 'ASTRID': {'MO': ('10:00', '12:00'), 'TH': ('12:00', '14:00'), 'SU': ('20:00', '21:00')}, 'ANDRES': {'MO': ('10:00', '12:00'), 'TH': ('12:00', '14:00'), 'SU': ('20:00', '21:00')}}
    '''
    lines=readFile(name)
    dicc={}
    for line in lines:
        key,value = userToDicc(line)
        dicc[key] = value
    #print(dicc)
    return dicc

def compareUsers(dicc):
    '''
    INPUT: A dictionary with the employee's name as key and the employee's schedule dictionary as value
    OUTPUT: A list, the elements are tuples with 3 values: employee's name 1, employee's name 2, how often they coincided in office

    Example:
    INPUT: {'RENE': {'MO': ('10:00', '12:00'), 'TU': ('10:00', '12:00'), 'TH': ('01:00', '03:00'), 'SA': ('14:00', '18:00'), 'SU': ('20:00', '21:00')}, 'ASTRID': {'MO': ('10:00', '12:00'), 'TH': ('12:00', '14:00'), 'SU': ('20:00', '21:00')}, 'ANDRES': {'MO': ('10:00', '12:00'), 'TH': ('12:00', '14:00'), 'SU': ('20:00', '21:00')}}
    OUTPUT: [('RENE', 'ASTRID', '2'), ('RENE', 'ANDRES', '2'), ('ASTRID', 'ANDRES', '3')]
    '''
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
    #print(comparation)
    return comparation

def compareHours(hours1,hours2):
    '''
    INPUT: 2 values: 1st -> a tuple with two hours from an employee
                     2nd -> a tuple with two hours from another employee
           NOTE: hours 1st value is the beginning of the shift and the 2nd is the end of it.

    OUTPUT: Boolean (True of False) if the hours coincided

    Example1:
    INPUT: 1st -> ('10:00', '12:00')
           2nd -> ('10:00', '12:00')
    OUTPUT: True

    Example2:
    INPUT: 1st -> ('10:00', '12:00')
           2nd -> ('01:00', '03:00')
    OUTPUT: False
    '''
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
    '''
    INPUT: 2 values: 1st -> A dictionary with an employee's name as key and the employee's schedule dictionary as value
                     2nd -> A dictionary with other employee's name as key and the employee's schedule dictionary as value
    OUTPUT:  How often they coincided in office as int

    Example:
    INPUT: 1st -> 'RENE': {'MO': ('10:00', '12:00'), 'TU': ('10:00', '12:00'), 'TH': ('01:00', '03:00'), 'SA': ('14:00', '18:00'), 'SU': ('20:00', '21:00')}
           2nd -> 'ASTRID': {'MO': ('10:00', '12:00'), 'TH': ('12:00', '14:00'), 'SU': ('20:00', '21:00')}
    OUTPUT: 2
    '''
    c=0
    for key in dicc1:
        if key in dicc2:
            if compareHours(dicc1[key],dicc2[key]):
                c+=1
    #print(c)
    return c

def formatResults(results):
    '''
    INPUT:  A list, the elements are tuples with 3 values: employee's name 1, employee's name 2, how often they coincided in office
    OUTPUT: NO OUTPUT -> just format the values from the input and print it.

    Example:
    INPUT: [('RENE', 'ASTRID', '2'), ('RENE', 'ANDRES', '2'), ('ASTRID', 'ANDRES', '3')]
    OUTPUT: RENE-ASTRID:2
            RENE-ANDRES:2
            ASTRID-ANDRES:3
    '''
    for result in results:
        name1 = result[0]
        name2 = result[1]
        times = result[2]
        print(name1+"-"+name2+":"+times)


def runProgram(name):
    '''
    INPUT: The name of the file as string (without extension)
    OUTPUT: NO OUTPUT -> just print the results

    NOTE: This function initialize the program

    '''
    employees_dicc = fileToDicc(name)
    results = compareUsers(employees_dicc)
    formatResults(results)

runProgram("file")