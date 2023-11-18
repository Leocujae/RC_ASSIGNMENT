import socket
import sys

def connect_to_server(server_host, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        print('Conectado a:', (server_host, server_port))
        return client_socket
    except IOError:
        print("no se pudo establecer conexion con el servidor")
        sys.exit(1)

def send_request(client_socket, filename, server_host):
    request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    client_socket.sendall(request.encode())

def receive_data(client_socket):
    final_data = ""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        final_data += data.decode()
    return final_data

def close_connection(client_socket):
    client_socket.close()

def main():
    server_host = "localhost"
    server_port = 8000
    filename = "assignment_1/node_modules/@popperjs/core/url.txt"

    client_socket = connect_to_server(server_host, server_port)
    send_request(client_socket, filename, server_host)
    received_data = receive_data(client_socket)
    close_connection(client_socket)

    print("The data:", received_data)

if __name__ == "__main__":
    main()