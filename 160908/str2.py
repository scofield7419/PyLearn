#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 'Hi, %s. ' % 'there'
print(x)

x = 'Hi, %s, you have $%d. ' % ('micheal',10000)
print(x)


x = 'Hi, %f. ' % 12.3423423
print(x)

x = '哈哈哈，%x' % 1024
print(x)

#如果你不太确定应该用什么，%s 永远起作用，它会把任何数据类型转换为字符串
x = 'Age: %s. Gender: %s' % (25, True)
print(x)

#字符串里面的%是一个普通字符,候就需要转义，用%%来表示一个%
x =  'growth rate: %d %%' % 7
print(x)