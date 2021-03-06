#hashlib
#Python 的 hashlib 提供了常见的摘要算法，如 MD5，SHA1 等等。
#什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函
#数，把任意长度的数据转换为一个长度固定的数据串（通常用 16 进制的字符串表示）。


#MD5 是最常见的摘要算法，速度很快，生成结果是固定的 128 bit 字节，通常用一个 32 位的 16 进制字符串表示。
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


#如果数据量很大，可以分块多次调用 update()，最后计算的结果是一样
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())




#另一种常见的摘要算法是 SHA1，调用 SHA1 和调用 MD5 完全类似：
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
#SHA1 的结果是 160 bit 字节，通常用一个 40 位的 16 进制字符串表示。

















