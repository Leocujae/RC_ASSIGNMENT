import signal
import socket
import threading

class ProxyServer:
    def __init__(self, config):
        # Shutdown on Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown)

        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to a public host and a port
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))

        self.serverSocket.listen(10)  # Become a server socket
        self.__clients = {}

    def shutdown(self, signum, frame):
        # Implement shutdown logic
        pass

    def _getClientName(self, client_address):
        # Implement client naming logic
        pass

    def start(self):
        while True:
            # Establish the connection
            (clientSocket, client_address) = self.serverSocket.accept()

            d = threading.Thread(
                name=self._getClientName(client_address),
                target=self.proxy_thread,
                args=(clientSocket, client_address)
            )
            d.setDaemon(True)
            d.start()

    def proxy_thread(self, conn, client_address):
        request = conn.recv(config['MAX_REQUEST_LEN'])
        str_request = request.decode()
        first_line = str_request.split('\n')[0]
        url = first_line.split(' ')[1]

        http_pos = url.find("://")
        if (http_pos == -1):
            temp = url
        else:
            temp = url[(http_pos + 3):]

        port_pos = temp.find(":")
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos == -1 or webserver_pos < port_pos):
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int((temp[(port_pos + 1):])[:webserver_pos - port_pos - 1])
            webserver = temp[:port_pos]

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(config['CONNECTION_TIMEOUT'])
        s.connect((webserver, port))
        s.sendall(request)

        while True:
            data = s.recv(config['MAX_REQUEST_LEN'])

            if len(data) > 0:
                conn.send(data)
            else:
                break

# Define your configuration
config = {
    'HOST_NAME': 'localhost',
    'BIND_PORT': 8000,
    'MAX_REQUEST_LEN': 8048,
    'CONNECTION_TIMEOUT': 10
}

# Create and start the proxy server
proxy_server = ProxyServer(config)
proxy_server.start()