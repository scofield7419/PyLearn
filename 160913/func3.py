#偏函数
#Python 的 functools 模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
import functools
int2 = functools.partial(int ,base=2)
print(int2('1011101110'))
#把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


