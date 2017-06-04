#Author:lzf
#_*_coding:utf-8_*_

import  socket
# client=socket.socket()
# client.connect(('192.168.2.55',6969))
# while True:
#         msg=input(">>:").strip()
#         client.send(msg.encode("utf-8")) #3中要用比特流穿数据
#         data=client.recv(1024) #大小，字节
#         print("recv:",data.decode())
#
# client.close()

client=socket.socket()
client.connect(('localhost',9998))

while True:
    cmd = input(">>:").strip()

    if len(cmd)==0: continue
    client.send(cmd.encode("utf-8"))
    # cmd_res = client.recv(1024)
    cmd_res_size = client.recv(1024)
    print("命令结果:",cmd_res_size)
    received_size = 0
    received_data = b''
    # print(cmd_res.decode())
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data) #每次收到的有可能小予1024，所以必须用len判断真实的长度
        received_data +=data
    else:
        print("cmd_res receive done...",received_size)
        print(received_data.decode())
client.close()