# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice03.py 
@time: 2020/09/25
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# CRAPS赌博游戏
from random import randint

def roll_dices():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    dice_sum = dice1 + dice2
    return dice_sum

def main():
    list1 = [7, 11]
    list2 = [2, 3, 12]
    dice1 = roll_dices()
    if dice1 in list1:
        result = True
    elif dice1 in list2:
        result = False
    else:
        dice2 = 0
        while dice2 != 7 and dice2 != dice1:
            dice2 = roll_dices()
            if dice2 == 7:
                result = False
            elif dice2 == dice1:
                result = True
    return result

if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(main())
    print(list)