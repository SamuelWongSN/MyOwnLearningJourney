'''
 # -*- coding: utf-8 -*-
 @Time    : 4/21/2020 12:02 AM
 @Author  : 思侬
 @Email   : robeenwang@163.com
 @File    : ex9_7.py
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

class Admin(User):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname)
        self.previlige = ['can add post','can delete post','can ban user']
    def show_previleges(self):
        for pre in self.previlige:
            print('-' + pre)

new_admin = Admin('sn','wong')
print(new_admin.firstname + ' ' + new_admin.lastname)
new_admin.show_previleges()