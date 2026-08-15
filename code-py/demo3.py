import socket
#客户端
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',10086))
# data = client_socket.recv(1024).decode('utf-8')
# print(f'{data}')
# client_socket.send('哈喽哈哈哈哈'.encode('utf-8'))
#encode编码 把字符串转成二进制   decode解码 把二进制转成字符串
with open('D:/wyf/封面制作.txt','rb') as src_file:
    while True:
        file_data = src_file.read(8192)
        client_socket.send(file_data)
        if len(file_data) == 0 :
            break

client_socket.close()