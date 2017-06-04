#Author:lzf
#_*_coding:utf-8_*_

import socket,os

# server= socket.socket()
# server.bind(('192.168.2.55',6969)) #绑定要监听的端口
# server.listen()#监听 最大连接，允许最大排队数
#
# print("我要开始等电话了")
# while True:
#     conn,addr=server.accept() #等电话打进来
#     #conn就是客户端连过来而在服务器围棋生成的一个连接实例，因为服务器会有很多等待
#     print(conn,addr)
#
#     print("电话来了")
#     while True:
#         data=conn.recv(1024)
#         print("recv:",data)
#         if not data:
#             print("client has lost...")
#         conn.send(data.upper())
# server.close()


server=socket.socket()
server.bind(('localhost',9998))
server.listen()
while True:
    conn,addr=server.accept()
    print("new conn:",addr) 
    while True:
        data=conn.recv(1024)
        if not data:
            print("客户端断开")
            break
        print("执行指令:",data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res)==0:
         cmd_res = b"abc"
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))    #先发客户端

        conn.send(cmd_res.encode("utf-8"))
server.close()