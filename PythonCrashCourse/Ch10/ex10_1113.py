'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 2:01 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex10_1113.py
 @Software: PyCharm
'''

import json
def setFnum(filename,name,num):
    try:
        with open(filename) as file:
            fnumdict = json.load(file)
    except:
        print("Can not find doc.")
    else:
        fnumdict[name.lower()] = num
        with open(filename,'w') as file:
            json.dump(fnumdict,file)
        print("Congurations!you already be our client.")

def getFnum(filename,name):
    try:
        with open(filename) as file:
            fnumdict = json.load(file)
    except:
        pass
    else:
        return fnumdict[name]

def jundgeUser(filename,name):
    try:
        with open(filename) as file:
            fnumdict = json.load(file)
    except:
        pass
    else:
        if name.lower() in fnumdict.keys():
            return True
        else:
            return False

def favnum():
    filename = 'Fnum.json'
    name = input("Hello,Please input your name: ")
    if jundgeUser(filename,name):
        print("wow! You have sign up!")
        nums = getFnum(filename,name)
        print("Your favourite number is "+str(nums))
    else:
        print("Sorry,you are not our client.")
        flag = input("Would you like to sign up? y/n")
        if flag == 'y':
            num = input("Please input your favourite number: ")
            setFnum(filename,name,num)
        elif flag == 'n':
            print("Thank you.")
        else:
            print("input wrong letter.")

favnum()