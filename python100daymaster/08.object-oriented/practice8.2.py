# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice8.2.py 
@time: 2020/09/27
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。

from math import sqrt

class Point():
    def __init__(self, x=0, y=0):
        '''
        :param x: pos of this point
        :param y: pos of this point
        '''
        self.x = x
        self.y = y

    def move_to(self, x, y):
        '''
        移动到指定坐标
        :param x: target pos
        :param y: target pos
        :return: None
        '''
        self.x = x
        self.y = y

    def move_by(self, x, y):
        '''
        按坐标增量移动
        :param x:
        :param y:
        :return:
        '''
        self.x += x
        self.y += y

    def distance(self, p):
        '''
        compute distance between self and this point
        :param x: target point
        :param y: target point
        :return: distance
        '''
        dis = sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
        return dis

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance(p2))

if __name__ == '__main__':
    main()