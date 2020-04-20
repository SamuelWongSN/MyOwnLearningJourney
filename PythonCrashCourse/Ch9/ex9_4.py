'''
 # -*- coding: utf-8 -*-
 @Time    : 4/20/2020 6:02 PM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex9_4.py
 @Software: PyCharm
'''

class User():
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname  = lastname
        self.age = 0
        self.country = ''
        self.login_attemps = 0
    def incresel(self):
        self.login_attemps += 1
    def resetl(self):
        self.login_attemps = 0
ss = User('wang','sin')
print(ss.login_attemps)
ss.incresel()
ss.incresel()
print(ss.login_attemps)
ss.resetl()
print(ss.login_attemps)