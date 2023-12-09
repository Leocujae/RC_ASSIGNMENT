from socket import *
import traceback

def recibir_datos_cliente(tcpCliSock):
    print('\n\nListo para servir...')
    addr = tcpCliSock.getpeername()
    print('Recibida una conexión desde:', addr)
    mensaje = tcpCliSock.recv(2048).decode()
    print(mensaje)
    return mensaje

def extraer_nombre_archivo_desde_mensaje(mensaje):
    nombre_archivo = mensaje.split()[1].partition("/")[2]
    print(nombre_archivo)
    archivo_existente = "false"
    archivo_a_usar = "/" + nombre_archivo
    print('--------------------------------------------')
    print(archivo_a_usar)
    print('--------------------------------------------')
    return archivo_existente, archivo_a_usar

def servir_desde_cache_o_conectar_al_servidor(tcpCliSock, archivo_a_usar):
    try:
        # Verificar si el archivo existe en la caché
        archivo_existente = "true"
        with open(archivo_a_usar[1:], "rb") as f:
            datos_salida = f.readlines()
        
        # El ProxyServer encuentra un acierto en la caché y genera un mensaje de respuesta
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        tcpCliSock.send("\r\n".encode())
        for linea in datos_salida:
            tcpCliSock.send(linea + "\r\n".encode())
        print('Leído desde la caché')
    except IOError:
        if archivo_existente == "false":
            # Crear un socket en el servidor proxy
            c = socket(AF_INET, SOCK_STREAM)
            hostn = archivo_a_usar.replace("www.","",1)
            print('--------------------------------------------')
            print(hostn)
            print('--------------------------------------------')
            try:
                # Conectar al socket al puerto 80
                c.connect((hostn, 80))
                print('----Conectado----')
                # Crear un archivo temporal en este socket y solicitar al puerto 80 el archivo solicitado por el cliente
                fileobj = c.makefile('rwb', 0)
                fileobj.write("GET ".encode() + "http://".encode() + archivo_a_usar.encode() + " HTTP/1.0\n\n".encode())
                # Leer la respuesta en el búfer
                data = fileobj.read()
                # Crear un nuevo archivo en la caché para el archivo solicitado.
                # También enviar la respuesta en el búfer al socket del cliente y el archivo correspondiente en la caché
                with open("./" + archivo_a_usar,"wb") as tmpFile:
                    tmpFile.write(data)
                tcpCliSock.send(data)
            except Exception as e:
                print("Solicitud no válida")
                traceback.print_exc()
                print('Excepción: ', e)
        else:
            # Mensaje de respuesta HTTP para archivo no encontrado
            print("ERROR DE RED")

def servidor_proxy():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(("localhost", 8000))
    tcpSerSock.listen(1)

    while True:
        try:
            tcpCliSock, addr = tcpSerSock.accept()
            mensaje = recibir_datos_cliente(tcpCliSock)
            
            archivo_existente, archivo_a_usar = extraer_nombre_archivo_desde_mensaje(mensaje)

            servir_desde_cache_o_conectar_al_servidor(tcpCliSock, archivo_a_usar)

            # Cerrar el socket del cliente
            tcpCliSock.close()
        except KeyboardInterrupt:
            print("\nServidor Proxy apagándose.")
            break
        except Exception as e:
            print("Se produjo un error:")
            traceback.print_exc()
            print('Excepción: ', e)

    tcpSerSock.close()

if __name__ == "__main__":
    servidor_proxy()
