#network


#TCP/IP

# 导入 socket 库:
import socket

# 创建一个 socket:
#AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6
#SOCK_STREAM 指定使用面向流的 TCP 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接,我们连接新浪服务器的代码:
s.connect(('www.sina.com.cn', 80))#注意参数是一个 tuple，包含地址和端口号
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')


#TCP 连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先
#发谁后发，怎么协调，要根据具体的协议来决定。例如，HTTP 协议规
#定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。


#接收新浪服务器返回的数据
# 接收数据:
buffer = []
while True:#在一个 while 循环中反复接收，直到 recv()返回空数据
	# 每次最多接收 1k 字节:调用 recv(max)方法，一次最多接收指定的字节数
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

# 关闭连接:
s.close()


#把 HTTP 头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
	f.write(html)





#UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))

#但是不需要调用 listen()方法，而是直接接收来自任何客户端的数据：
print('Bind UDP on 9999...')
while True:
	# 接收数据:
	data, addr = s.recvfrom(1024)
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)


#客户端使用 UDP 时，首先仍然创建基于 UDP 的 Socket，然后，不需要调用 connect()，直接通过 sendto()给服务器发数据：

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
	# 发送数据:
	s.sendto(data, ('127.0.0.1', 9999))
	# 接收数据:
	print(s.recv(1024).decode('utf-8'))
s.close()




#UDP 的使用与 TCP 类似，但是不需要建立连接。此外，服务器绑定 UDP
#端口和 TCP 端口互不冲突，也就是说，UDP 的 9999 端口与 TCP 的 9999
#端口可以各自绑定。







