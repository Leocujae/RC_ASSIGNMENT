from socket import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('localhost', 12000)
clientSocket.settimeout(1.0)

num_pings = 10
for i in range(num_pings):
    # Mensaje a enviar al servidor
    message = f"Ping {i + 1}"

    try:
        start_time = time.time()
        clientSocket.sendto(message.encode(), serverAddress)
        response, serverAddress = clientSocket.recvfrom(1024)

        end_time = time.time()
        rtt = end_time - start_time
        print(f"Respuesta del servidor: {response.decode()}, RTT: {rtt:.6f} segundos")

    except timeout:
        print("Tiempo de espera agotado")

clientSocket.close()