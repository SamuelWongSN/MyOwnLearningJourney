# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice7.2.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random
def main(m=6):
    char = '1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
    n = len(char)
    list = ''
    for _ in range(m):
        list += char[random.randint(0, n-1)]
    print(list)

if __name__ == '__main__':
    main(10)