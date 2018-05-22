import time
import socket

# ip и порт
host = socket.gethostbyname(socket.gethostname())
port = 8080

# список клиентов
clients =[]

# создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

# переменая quit для цикла while, в которая будет
# отвечать за основную работу скрипта
quit = False
print("---Server Started---")


while not quit:
    try:

        data, addr = server_socket.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)


        # задание времени получения
        time_string = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        data_string = data.decode("utf-8")

        # протоколирование работы сервера  в log файл
        log_string = "\n[" + addr[0] + "]=[" + time_string + "]/" + data_string

        # Стандартный вывод:
        print(log_string)


        # отправка другим клиентам
        for i in clients:
            if addr != i:
                server_socket.sendto(data, i)

    except:
        print("\n---Server Stopped---")
        quit = True


server_socket.close()