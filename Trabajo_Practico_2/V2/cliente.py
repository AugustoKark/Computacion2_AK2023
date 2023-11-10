import requests
from PIL import Image
import io
import base64
import argparse

#Ejecucion del cliente:
#python3 cliente.py -i 127.0.0.1 -p 8080



parser = argparse.ArgumentParser(description='Cliente para enviar imágenes al servidor.')
parser.add_argument('-i', '--ip', type=str, default='127.0.0.1', help='Dirección IP del servidor')
parser.add_argument('-p', '--port', type=int, default=8080, help='Puerto del servidor')
args = parser.parse_args()


servidor = f'http://{args.ip}:{args.port}'
ruta_servicio = '/procesar'


# ruta_imagen = 'elon.jpeg'
ruta_imagen = input("Ingrese el nombre de la imagen a procesar: ")

imagen = Image.open(ruta_imagen)


buffer = io.BytesIO()
imagen.save(buffer, format="JPEG")

# Enviar la imagen al servidor
archivo = {'imagen': buffer.getvalue()}
respuesta = requests.post(f'{servidor}{ruta_servicio}', files=archivo)

# Manejar la respuesta del servidor
datos_respuesta = respuesta.json()
estado = datos_respuesta["estado"]

if estado == "completado":
   
    imagen_procesada_base64 = datos_respuesta["imagen_procesada"]
    imagen_procesada_bytes = base64.b64decode(imagen_procesada_base64)

    with open("imagen_procesada.jpg", "wb") as f:
        f.write(imagen_procesada_bytes)
    
    print("Procesamiento completado. Imagen guardada como imagen_procesada.jpg.")

