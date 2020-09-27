# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice8.1.py 
@time: 2020/09/27
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习1：定义一个类描述数字时钟。

import time
class Clock():
    def __init__(self, hour, mit, sec):
        self.hour = hour
        self.mit = mit
        self.sec = sec

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.mit += 1
            if self.mit == 60:
                self.mit = 0
                self.hour = (self.hour+1)%24

    def show(self):
        print('%02d:%02d:%02d' % (self.hour, self.mit, self.sec))

def main():
    c = Clock(23, 59, 50)
    while True:
        c.show()
        time.sleep(1)
        c.run()

if __name__ == '__main__':
    main()