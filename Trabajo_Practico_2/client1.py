import http.client
import argparse

'''
Ejecutar el cliente:

$ python3 client1.py elon.jpg 
            o
$ python3 client1.py elon.jpg -p 8080
            o
$ python3 client1.py elon.jpg -i 127.0.0.1 -p 8080

'''

def send_image(image_path, server_host, server_port):
  
    with open(image_path, 'rb') as file:
        image_data = file.read()

    headers = {'Content-type': 'image/jpeg'}
    conn = http.client.HTTPConnection(server_host, server_port)
    conn.request("POST", '/', body=image_data, headers=headers)

    response = conn.getresponse()

    if response.status == 200:

        grayscale_image_data = response.read()

        with open('nueva_imagen.jpg', 'wb') as new_image_file:
            new_image_file.write(grayscale_image_data)

        print("Imagen en escala de grises guardada como nueva_imagen.jpg")
    else:
        print(f"Error en la respuesta del servidor: {response.status} {response.reason}")

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cliente para Tp2 - procesa imagenes')
    parser.add_argument('image_path', help='Ruta de la imagen a enviar')
    parser.add_argument('-i', '--ip', default='localhost', help='Dirección del servidor')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Puerto del servidor')
    args = parser.parse_args()


    send_image(args.image_path, args.ip, args.port)
