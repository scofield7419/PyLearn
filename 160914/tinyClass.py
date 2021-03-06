#tiny class

#type()动态创建
#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

class Hello(object):
	def hi(self,name = 'scott'):
		print('hello , %s.'%name)
		
#执行结果就是动态创建出一个 Hello 的 class 对象
h = Hello()
h.hi()
print(type(Hello))
print(type(h))
#type()函数可以查看一个类型或变量的类型，Hello 是一个 class，它的
#类型就是 type，而 h 是一个实例，它的类型就是 class Hello。
#class 的定义是运行时动态创建的，而创建 class 的方法就是使用type()函数。
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，

#我们可以通过 type()函数创建出 Hello 类，而无需通过 classHello(object)...的定义：
def fn(self,name = 'scotte'):
	print('adw %s' % name)

hey = type('hey',(object,),dict(hello = fn))# 创建 hey class
h = hey()
h.hello()
print(type(hey))
print(type(h))






# metaclass，直译为元类，简单的解释就是：必须根据 metaclass 创建出类，所以：先定义 metaclass，然后创建类。
#连接起来就是：先定义 metaclass，就可以创建类，最后创建实例
#，metaclass 允许你创建类或者修改类。换句话说，你可以把类看成是 metaclass 创建出来的“实例”。

# metaclass 是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add'] = lambda self ,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)


#在定义类的时候还要指示使用 ListMetaclass 来定制类，传入关键字参数 metaclass：
class MyList(list,metaclass = ListMetaclass):
	pass

print(type(MyList))
print(type(MyList()))

#ORM 全称“Object Relational Mapping”，即对象-关系映射，就是把关系
#数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作 SQL 语句。










