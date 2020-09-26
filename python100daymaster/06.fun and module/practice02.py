# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice02.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
# 实现判断一个数是不是回文数的函数。
import time

def fun(n):
    flag = True
    n_str = str(n)
    m = len(n_str) // 2
    for i in range(m):
        if n_str[i] != n_str[-1-i]:
            flag = not flag
            break
    return flag

def fun2(n):
    temp = n
    total = 0
    while temp>0:
        total = total*10 + temp % 10
        temp //= 10
    return total == n

def main():
    n = int(input(':'))
    start = time.process_time()
    for _ in range(1000000):
        fun(n)
    end = time.process_time()
    t1 = end - start
    start = time.process_time()
    for _ in range(1000000):
        fun2(n)
    end = time.process_time()
    t2 = end - start
    print(t1, t2)

if __name__ == '__main__':
    main()