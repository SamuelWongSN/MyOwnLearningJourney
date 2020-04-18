# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:59:39 2020

@author: 思侬
"""

guide_list = ["Andrew Ng","Benjimin Franklin","老爆","Trump","Naruto"]
for i in guide_list:
    print("Dear " + i + ", I invite you have a dinner concerely.")
print(" ")
# 邀请以上嘉宾名单的人员来与我共享晚宴
    
print(guide_list[3] + " cannot come here.")
guide_list[3] = 'Doinb'
# 特朗普有事儿来不了了，嘉宾名单换成了硬币哥，希望他能来

for i in guide_list:
    print("Dear " + i + ", I invite you have a dinner concerely.")
print(" ")
# 继续发邀请
    
print("I find a bigger table");
guide_list.insert(0,'jj')
guide_list.insert(2,'grape')
guide_list.append("kugua")
for i in guide_list:
    print("Dear " + i + ", I invite you have a dinner concerely.")
print(" ")
# 我又找到了一个大的桌子，这样就可以邀请更多的人来了

print("The table was broken,I may only invite two guides.")
for i in range(6):
    print("I'm so sorry bro,hope you still happy," + guide_list.pop())
print(" ")
for i in guide_list:
    print("conguratulations bro,you could still come to my house," + i);
del guide_list[1]
guide_list.remove("jj")
print(guide_list)
# 完了，桌子坏了，只能邀请两个人了，so sad 但是jiji和andrewng 欢迎你们奥

# 以下内容为练习3-9
guide_list = ["jj","Andrew Ng","Benjimin Franklin","老爆","Trump","Naruto"]
print("I have invited " + str(len(guide_list)) + " friends.")