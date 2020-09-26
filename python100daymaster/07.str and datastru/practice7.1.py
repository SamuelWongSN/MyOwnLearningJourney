# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice7.1.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习1：在屏幕上显示跑马灯文字。

import os
import time

def main():
    content = 'I Love Python'
    while True:
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()