#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行注释是为了告诉 Linux/OS X 系统，这是一个 Python 可执行程序，Windows 系统会忽略这个注释；
#第二行注释是为了告诉 Python 解释器，按照 UTF-8 编码读取源代码

str = ord('A')
print(str)

str = ord('中')
print(str)

str = chr(66)
print(str)

str = chr(25991)
print(str)

#如果知道字符的整数编码，还可以用十六进制这么写 str：
print( '\u4e2d\u6587' )

#Python 的字符串类型是 str，在内存中以 Unicode 表示，一个字符
#对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把
#str 变为以字节为单位的 bytes。
x = b'ABC'
print(x)
#并且b'呵呵'是不允许的：SyntaxError: bytes can only contain ASCII literal characters.

#要注意区分'ABC'和 b'ABC'，前者是 str，后者虽然内容显示得和前者一
#样，但 bytes 的每个字符都只占用一个字节。
x = 'ABC'
print(x)

#1 个中文字符经过 UTF-8 编码后通常会占用 3 个字节，而 1 个英
#文字符只占用 1 个字节。

