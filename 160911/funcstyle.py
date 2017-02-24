#函数式编程
#函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

#函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言
#编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出
#就是确定的，这种纯函数我们称之为没有副作用

#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函
#数，还允许返回一个函数！

#由于 Python 允许使用变量，因此，Python 不是纯函数式编程语言。

#那么函数名是什么呢？函数名其实就是指向函数的变量！对于 abs()这
#个函数，完全可以把函数名 abs 看成变量，它指向一个可以计算绝对值的函数！


#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以
#接收另一个函数作为参数，这种函数就称之为高阶函数。

#一个最简单的高阶函数：
def add(x,y,f):
	return f(x)+f(y)






#map/reduce
def f(x):
	return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不
#但可以计算简单的 f(x)=x2，还可以计算任意复杂的函数，比如，把这个list 所有数字转为字符串：

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce 把一个函数作用在一个序列[x1, x2, x3, ...]
#上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算，其效果就是：
from functools import reduce
def add(x,y):
	return x*x*x*x + y*100

print(reduce(add,[1,2,3,4,5,6]))


#filter函数,过滤序列
#和 map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。
def isOdd(n):
	return n%2==1
print(list(filter(isOdd,[1,2,3,4,5,6,7,8,9,10])))


#sorted排序函数
print(sorted([123,122,12,42,4564,234]))
#此外，sorted()函数也是一个高阶函数，它还可以接收一个 key 函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([123,12,-2,12,-42,45,-64,234],key=abs))
#key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序。对比原始的 list 和经过 key=abs 处理过的 list：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))





#函数作为返回值
#。通常情况下，求和的函数是这样
def calc(*args):
	ax = 0
	for n in args:
		ax += n
	return ax
#如果不需要立刻求和，而是在后面的代码中
def lazy(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum
#当我们调用 lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy(1,2,3,4,5,6,7,12)
print(f)
print(f())#调用函数 f 时，才真正计算求和的结果：
#当 lazy 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。



#闭包
#个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了 f()才执行。
def count():
	fs = []
	for n in range(1,5):
		def f():
			return i*i
		fs.append(f)
	return fs

f1 , f2 ,f3=count()
print(f1())
print(f2())
print(f3())
#你可能认为调用 f1()，f2()和 f3()结果应该是 1，4，9，但实际结果是
#全部都是 9！原因就在于返回的函数引用了变量 i，但它并非立刻执行。等到 3 个函数都返回时，它们所引用的变量 i 已经变成了 3，因此最终结果为 9。




#匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
#匿名函数 lambda x: x * x 实际上就是：
def f(x):
	return x*x
#关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写 return，返回值就是该表达式的结果。

#也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x:x *x
print(f(6))

#同样，也可以把匿名函数作为返回值返回
def build(x,y):
	return lambda :x*x+y*y


