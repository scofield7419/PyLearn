# -*- coding: utf-8 -*-
#####list 列表########


classmates = ['scott','bob','scofield']
print(classmates)

y = len(classmates)
print(y)

print(classmates[1])

#获取倒数第x个元素
print(classmates[-2])

classmates.insert(3,'hystro')

print(classmates)

print(classmates.pop())

classmates[1] = 'Sarah'
print(classmates)

###混合#####
l = ['heheda',123,True]
print(l)

###二维#####
d = ['asp','php','jsp']
s  = ['python' , 'java' , d]
print(s)
