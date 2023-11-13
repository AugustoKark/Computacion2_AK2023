import http.server
import socketserver
from io import BytesIO
from PIL import Image
import multiprocessing
import queue
import argparse
import socket

'''
Ejecutar el servidor:

IPV4:
$ python3 server1.py -i 127.0.0.1 -p 8080

IPV6:
$ python3 server1.py -i ::1 -p 8080


'''


class GrayscaleConversionService:
    @staticmethod
    def convert_to_grayscale(image_data):
        image = Image.open(BytesIO(image_data)).convert('L')
        output_buffer = BytesIO()
        image.save(output_buffer, format="JPEG")
        return output_buffer.getvalue()

def grayscale_conversion_worker(request_queue, result_queue):
    grayscale_service = GrayscaleConversionService()

    while True:
        try:
            request_data = request_queue.get(timeout=1)  
        except queue.Empty:
            continue
        except KeyboardInterrupt:
            print("Proceso hijo: Interrupción de teclado recibida. Cerrando...")
            break

        if request_data is None:
            print("Proceso hijo: Señal para terminar el proceso")
            break  

        client_socket, image_data = request_data
        print(f"Proceso hijo: Recibida solicitud de cliente, imagen de {len(image_data)} bytes")
        grayscale_image_data = grayscale_service.convert_to_grayscale(image_data)
        result_queue.put((client_socket, grayscale_image_data))
        print(f"Proceso hijo: Imagen convertida y enviada al cliente")

class ConcurrentHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        image_data = self.rfile.read(content_length)

        request_data = (self.request, image_data)
        print("Servidor principal: Enviando solicitud al proceso hijo")
        request_queue.put(request_data)

        client_socket, grayscale_image_data = result_queue.get()
        print("Servidor principal: Recibida respuesta del proceso hijo")
        
        self.send_response(200)
        self.send_header("Content-Type", "image/jpeg")
        self.end_headers()
        self.wfile.write(grayscale_image_data)
        print("Servidor principal: Enviada respuesta al cliente")

        client_socket.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Tp2 - procesa imagenes')
    parser.add_argument('-i', '--ip', default='::', help='Dirección de escucha')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Puerto de escucha')
    args = parser.parse_args()

    IP = args.ip
    PORT = args.port

    # Crear un socket que admite tanto IPv4 como IPv6
    server_address = (IP, PORT)
    socket_family = socket.AF_INET6 if ":" in IP else socket.AF_INET

    socketserver.TCPServer.address_family = socket_family
    my_handler = ConcurrentHandler
    httpd = socketserver.TCPServer(server_address, my_handler)

   
    request_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=grayscale_conversion_worker, args=(request_queue, result_queue))
    process.start()
    print(f"Servidor principal: Abriendo servidor httpd en el puerto {PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
  
        request_queue.put(None)  
        process.join()

        httpd.server_close()
        print("Servidor principal: Servidor cerrado correctamente.")
