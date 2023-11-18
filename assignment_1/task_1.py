from socket import *

def handle_request(connectionSocket):
    try:
        # Recibir el mensaje de solicitud del cliente
        message = connectionSocket.recv(1024)
        
        # Extraer la ruta del objeto solicitado del mensaje
        # La ruta es la segunda parte del encabezado HTTP identificada como [1]
        message_str = message.decode('utf-8')  # Puedes ajustar el encoding según sea necesario
        filename = message_str.split()[1]
        print(filename)

        # Dado que la ruta extraída de la solicitud tiene una /, leemos desde el segundo carácter
        with open(filename[1:], 'rb') as file:
            outputdata = file.read()

        # Enviar una línea de encabezado HTTP al socket
        connectionSocket.sendall(bytes('HTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))

        # Enviar el contenido del archivo solicitado al cliente
        connectionSocket.sendall(outputdata)
        connectionSocket.sendall(bytes("\r\n", 'UTF-8'))

    except IOError:
        # Enviar un mensaje de respuesta para archivo no encontrado
        print('Archivo no encontrado')
        connectionSocket.sendall(bytes('HTTP/1.1 404 Not Found\r\n\r\n', 'UTF-8'))
        connectionSocket.sendall(bytes('<html><head><title>First Web Page</title></head><body><h1>404 Not Found</h1></body></html>\r\n', 'UTF-8'))

    finally:
        # Cerrar la conexión después de manejar la solicitud
        connectionSocket.close()

if __name__ == '__main__':
    # Crear un socket de servidor TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # El puerto debe ser > 1024 para evitar errores de permisos
    serverPort = 8000

    # Vincular el socket a una dirección y puerto
    serverSocket.bind(('localhost', serverPort))

    # Escuchar hasta 1 conexión
    serverSocket.listen(5)
    print('El servidor web está en funcionamiento en el puerto:', serverPort)

    while True:
        # Configurar una nueva conexión desde el cliente
        print('Listo para atender...')
        connectionSocket, addr = serverSocket.accept()
        handle_request(connectionSocket)