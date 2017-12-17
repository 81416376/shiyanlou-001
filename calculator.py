#!/usr/bin/env python3
import sys

#Personal Income Tax Exemption Value
PIT_EV = 3500
#Personal Salary
PER_SALARY = 0
#Personal Income Tax RATE
PIT_RATE = 0

#
def SALARY_CAL(x,y,z):
    PIT_DATA = x * y - z
    #return format(PIT_DATA,".2f")
    return PIT_DATA

def PIT_CAL(value):
    #value = 1500
    if value <= 1500:
        return SALARY_CAL(value,0.03,0)
    elif value <= 4500:
        return SALARY_CAL(value,0.1,105)
    elif value <= 9000:
        return SALARY_CAL(value,0.2,555)
    elif value <= 35000:
        return SALARY_CAL(value,0.25,1005)
    elif value <= 55000:
        return SALARY_CAL(value,0.3,2755)
    elif value <= 80000:
        return SALARY_CAL(value,0.35,5505)
    else:
        return SALARY_CAL(value,0.45,13505)

try:
    ARGV_LIST = sys.argv[1:]
    if not ARGV_LIST:
        #print("blank parameter")
        bypass
    #print(ARGV_LIST)
    for argv in ARGV_LIST:
        USER_LIST = argv.split(':')   
        USERID = int(USER_LIST[0])
        SALARY = int(USER_LIST[1])
        #PER_SALARY = format(PER_SALARY,".2f")
        #print("%d:%s" % (USERID,format(PER_SALARY,".2f")))
        if SALARY > 0:
            PER_SALARY = SALARY * (1 - 0.08 - 0.02 - 0.005 - 0.06)
            #print(PER_SALARY)
            if PER_SALARY <= PIT_EV:
                print("%d:%s" % (USERID,format(PER_SALARY,".2f")))
            else:
                print("%d:%s" % (USERID,format(PER_SALARY - PIT_CAL(PER_SALARY - PIT_EV),".2f")))
        else:
                print("""Parameter Error!!!
The salary must be a positive number.""")
except:
    print("Parameter Error")
