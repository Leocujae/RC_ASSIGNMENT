from socket import *
import threading

class ClientThread(threading.Thread):
    def __init__(self, connection_socket, address):
        threading.Thread.__init__(self)
        self.connection_socket = connection_socket
        self.address = address

        print('Nueva conexión', address)

    def run(self):
        while True:
            try:
                message = self.connection_socket.recv(1024)
                if not message:
                    break
                print("\nMensaje: ", message)
                data = str(message.decode())
                print("\nDecodificado: ", data)
                filename = data.split()[1]
                print("\nNombre de archivo:", filename[0:])
                with open(filename[0:], 'r') as file:
                    output_data = file.read()

                self.connection_socket.sendall(bytes('HTTP/1.1 200 OK\r\n\r\n', 'UTF-8'))
                for i in range(0, len(output_data)):
                    self.connection_socket.sendall(bytes(output_data[i], 'UTF-8'))
                self.connection_socket.sendall(bytes("\r\n", 'UTF-8'))
                self.connection_socket.shutdown(SHUT_WR)
                #self.connection_socket.close()

            except IOError:
                self.connection_socket.sendall(bytes('HTTP/1.1 404 Not Found\r\n\r\n', 'UTF-8'))
                self.connection_socket.sendall(bytes('<html><head><title>First Web Page</title></head><body><h1>404 Not Found</h1></body></html>\r\n', 'UTF-8'))
                self.connection_socket.shutdown(SHUT_WR)
                #self.connection_socket.close()

if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_port = 8000
    server_socket.bind(('localhost', server_port))
    server_socket.listen(5)
    threads = []

    while True:
        try:
            print('Listo para atender...')
            connection_socket, addr = server_socket.accept()
            client_thread = ClientThread(connection_socket, addr)
            client_thread.daemon = True
            client_thread.start()
            threads.append(client_thread)
        except error:
            print("Error de socket")
            break

    # El hilo principal espera a que todos los hilos terminen y luego cierra la conexión
    server_socket.close()