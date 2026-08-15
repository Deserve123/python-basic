import socket
#服务端
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #
server_socket.bind(('127.0.0.1',10086))
server_socket.listen(5)
accept_socket, client_info = server_socket.accept()
# accept_socket.send(b'hello world')   #b 把string除汉字转换成二进制
# data = accept_socket.recv(1024).decode('utf-8')
# print(f'服务端收到 来自{client_info}客户端的信息:{data}')
with open('./work_py/my.txt','wb') as dest_file:
    while True:
        file_data = accept_socket.recv(8192)
        if len(file_data) == 0:
            break
        dest_file.write(file_data)

accept_socket.close()


