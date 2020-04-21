'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 1:27 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex10_7pluscalculator.py
 @Software: PyCharm
'''

print("Please input two numbers, I will plus them.")
print("If you want to quit, Please input 'q' anytime.")

while True:
    num1 = input("Please input first number: ")
    if num1 == 'q':
        break
    else:
        try:
            num1 = int(num1)
        except:
            print("Wrong!Please input number.")
            continue
        else:
            num2 = input("Please input the second number: ")
            if num2 == 'q':
                break
            else:
                try:
                    num2 = int(num2)
                except:
                    print("Wrong!Please input number.")
                    continue
                else:
                    print("The plus is " + str(num1 + num2))