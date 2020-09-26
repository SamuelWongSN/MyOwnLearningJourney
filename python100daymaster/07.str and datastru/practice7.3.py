# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice7.3.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 练习3：设计一个函数返回给定文件名的后缀名。

def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if has_dot:
        return filename[pos:]
    else:
        return filename[pos+1:]

def main():
    suffix = get_suffix('love.txt')
    print(suffix)

if __name__ == '__main__':
    main()