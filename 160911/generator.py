#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的 list，从而节省大量的空间。在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。

#要创建一个 generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个 generator：
L = [x*x for x in range(11)]
g = (x *x for x in range(11))

for n in g:
	print(n)

#generator 非常强大。如果推算的算法比较复杂，用类似列表生成式的 for循环无法实现的时候，还可以用函数来实现。
#斐波拉契数列（Fibonacci）
def fib(max):
	n ,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n +=1
	return 'done'

print(fib(10))
#要把 fib 函数变成generator，只需要把 print(b)改为 yield b 就可以
#如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator：
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n+=1
	return 'done'
print(fib(10))#不用这种方式
for n in fib(10):#fib()是一个生成器
	print(n)

#发现拿不到 generator 的 return 语句的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中：
