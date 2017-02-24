#collection
#collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。


#namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x,p.y)
#namedtuple 是一个函数，它用来创建一个自定义的 tuple 对象，并且规
#定了 tuple 元素的个数，并可以用属性而不是索引来引用 tuple 的某个元素。

#可以验证创建的 Point 对象是 tuple 的一种子类：
print(isinstance(p,Point))
print(isinstance(p,tuple))




#deque
#deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
#deque 除了实现 list 的 append()和 pop()外，还支持 appendleft()和
#popleft()，这样就可以非常高效地往头部添加或删除元素。



#defaultdict
#使用 dict 时，如果引用的 Key 不存在，就会抛出 KeyError。如果希望
#key 不存在时，返回一个默认值，就可以用 defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1 存在
print(dd['key2']) # key2 不存在，返回默认值




#OrderedDict
#使用 dict 时，Key 是无序的。在对 dict 做迭代时，我们无法确定 Key的顺序。
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict 的 Key 是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict 的 Key 是有序的
#注意，OrderedDict 的 Key 会按照插入的顺序排列，不是 Key 本身排序：




#Counter
#Counter 是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)
#Counter 实际上也是 dict 的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。














