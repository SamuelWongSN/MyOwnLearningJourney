# -*- coding:utf-8 _*-
""" 
@author: WangSN
@license: Apache Licence 
@file: practice03.py 
@time: 2020/09/26
@contact: samuel1997wang@gmail.com
@site:  
@software: PyCharm 
"""
def is_prime(n):
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = not flag
            break
    return flag

def main():
    n = int(input(':'))
    print(is_prime(n))

if __name__ == '__main__':
    main()