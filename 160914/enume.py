#enumerate
#Enum 类,Enum 可以把一组相关常量定义在一个 class 中，且 class 不可变，而且成员可以直接比较。


from enum import Enum,unique

Month = Enum('Month' , ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)


#如果需要更精确地控制枚举类型，可以从 Enum 派生出自定义类：
@unique #@unique 装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
	Sun = 0 
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat  =6

print(Weekday.Sun)
print(Weekday['Fri'])
print(Weekday.Sat.value)


