a = 100
if a>= 0:
	print(a)
else:
	print(-a)
print('\n')
#演示字符串中包含' 以及“&'的情况
print("I'am ok!")
print('I\'am \"ok\"!')

#当字符串中有一些关键符号时，可用转移字符
#转义字符\可以转义很多字符，比如\n 表示换行，\t 表示制表符，字符\
#本身也要转义

#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，
#Python 还允许用 r''表示''内部的字符串默认不转义
print(r'\\t')


#如果字符串内部有很多换行，用\n 写在一行里不好阅读，为了简化，
#Python 允许用'''...'''的格式表示多行内容,...表示内容

print('''line1
line2
line3''')

#接用 True、False表示布尔值（请注意大小写）

print(3>2)

print(3>2 and False)

print(3>2 and True)\

print(3>2 or False)

print(not 3>2)

print(None)