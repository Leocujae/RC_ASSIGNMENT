from socket import *
import time

# Crear un socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Definir la dirección del servidor y el puerto
serverAddress = ('localhost', 12000)

# Configurar el tiempo de espera en 1 segundo
clientSocket.settimeout(1.0)

# Número total de pings
num_pings = 10

# Inicializar variables para estadísticas
rtt_min = float('inf')  # RTT mínimo inicializado a infinito
rtt_max = 0.0  # RTT máximo inicializado a cero
rtt_total = 0.0  # Suma de RTTs inicializada a cero
paquetes_perdidos = 0

for i in range(num_pings):
    # Mensaje a enviar al servidor
    message = f"Ping {i + 1}"

    try:
        # Tiempo de inicio del envío
        start_time = time.time()

        # Enviar el mensaje al servidor
        clientSocket.sendto(message.encode(), serverAddress)

        # Esperar recibir la respuesta del servidor
        response, serverAddress = clientSocket.recvfrom(1024)

        # Tiempo de fin del envío
        end_time = time.time()

        # Calcular el tiempo de ida y vuelta (RTT)
        rtt = end_time - start_time

        # Actualizar estadísticas
        rtt_total += rtt
        rtt_min = min(rtt_min, rtt)
        rtt_max = max(rtt_max, rtt)

        # Imprimir la respuesta del servidor y el RTT
        print(f"Respuesta del servidor: {response.decode()}, RTT: {rtt:.6f} segundos")

    except timeout:
        # Si se produce un tiempo de espera, contar como paquete perdido
        print("Tiempo de espera agotado")
        paquetes_perdidos += 1

# Calcular estadísticas finales
rtt_promedio = rtt_total / num_pings
tasa_perdida = (paquetes_perdidos / num_pings) * 100

# Imprimir estadísticas finales
print("\nEstadísticas finales:")
print(f"RTT mínimo: {rtt_min:.6f} segundos")
print(f"RTT máximo: {rtt_max:.6f} segundos")
print(f"RTT promedio: {rtt_promedio:.6f} segundos")
print(f"Tasa de pérdida de paquetes: {tasa_perdida:.2f}%")

# Cerrar el socket del cliente
clientSocket.close()