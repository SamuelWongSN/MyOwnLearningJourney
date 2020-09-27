# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: case7.1.py 
@time: 2020/09/27
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 案例1：双色球选号。 略 没啥意思
# 案例2：约瑟夫环问题。
def main():
    people = [True] * 30
    pos = 0
    num = 1
    times = 15
    while times:
        if people[pos]:
            num += 1
        if num == 9:
            people[pos] = False
            times -= 1
            num = 1
        pos = (pos + 1) % 29
    print(people)

if __name__ == '__main__':
    main()