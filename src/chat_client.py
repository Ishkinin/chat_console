import socket
import time
import threading

# globe tmp
shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode('utf-8'))
                time.sleep(0.2)
        except:
            pass


# ip, порт и сервер
host = socket.gethostbyname(socket.gethostname())
port = 0
server = ("127.0.1.1", 8080)

# создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((host, port))
client_socket.setblocking(0)

# ввод пользователя
nickname = input("Enter nickname: ")

# создание потока
rT = threading.Thread(target=receving, args=("RecvThread", client_socket))
rT.start()


# отпрвка сообщения
while shutdown == False:
    if join == False:
        client_socket.sendto(("[" + nickname + "] => join chat ").encode("utf-8"), server)
        join = True
    else:
        try:

            message = input("enter message: ")

            if message != "":
                client_socket.sendto(("[" + nickname + "] :: " + message).encode("utf-8"), server)

                time.sleep(0.2)


        except:
            client_socket.sendto(("[" + nickname + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
client_socket.close()

