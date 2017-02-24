#test debug
#Python 内置了一套异常处理机制，来帮助我们进行错误处理。

try:
	print('try~~~')
	r = 10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally~~')
print('end')



#记录错误,Python 内置的 logging 模块可以非常容易地记录错误信息：
import logging

def fool(s):
	return 10/int(s)

def bar(s):
	return fool(s)*2

def main():
	try:
		bar('0')
	except Exception as e :
		logging.exception(e)

main()
print('end')#通过配置，logging 还可以把错误记录到日志文件里，方便事后排查。


#抛出错误,如果要抛出错误，首先根据需要，可以定义一个错误的 class，选择好继
#承关系，然后，用 raise 语句抛出一个错误的实例：
class FooError(VulueError):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' %s)
	return 10/n

foo('0')
#如果可以选择 Python已有的内置的错误类型（比如 ValueError，TypeError），尽量使用 Python内置的错误类型。

#最后，我们来看另一种错误处理的方式：
def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' %s)
	return 10/n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('valueerror')
		raise

bar()

#在 bar()函数中，我们明明已经捕获了错误，但是，打印一个 ValueError!
#后，又把错误通过 raise 语句抛出去了，这不有病么？

#其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记
#录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错
#误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。



#断言
def foo(s):
	n = int(s)
	assert n !=0 , 'n is zero'
	return 10/n

def main():
	foo('0')

#assert 的意思是，表达式 n != 0 应该是 True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#如果断言失败，assert 语句本身就会抛出 AssertionError：
#当然啦，程序中如果到处充斥着 assert，和 print()相比也好不到哪去。

#不过，启动 Python 解释器时可以用-O 参数来关闭 assert，关闭后，你可以把所有的 assert 语句当成 pass 来看。
#$ python3 -O err.py



#logging,把 print()替换为 logging 是第 3 种方式，和 assert 比，logging 不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n  = %d'%n)
print(10/n)

#这就是 logging 的好处，它允许你指定记录信息的级别，有 debug，info，
#warning，error 等几个级别，当我们指定 level=INFO 时，logging.debug
#就不起作用了。同理，指定 level=WARNING 后，debug 和 info 就不起作用
#了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后
#统一控制输出哪个级别的信息。




#pdb
#,第 4 种方式是启动 Python 的调试器 pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

#$ python3 -m pdb err.py
#n,单步，p x查看变量,c,继续运行



#pdb.set_trace()
#这个方法也是用 pdb，但是不需要单步执行，我们只需要 import pdb，
#然后，在可能出错的地方放一个 pdb.set_trace()，就可以设置一个断点：

import pdb

s= '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10/n)



#如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的 IDE。目前比较好的 Python IDE 有 PyCharm：





#单元测试
#如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。
#单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。




#文档测试


