from flask import Flask, request, jsonify
from multiprocessing import Process, Semaphore, Queue
from PIL import Image
import io
import base64
import argparse


#Ejecucion del servidor:
#python3 servidor.py -i 0.0.0.0 -p 8080


app = Flask(__name__)


sem = Semaphore(value=1)

def procesar_imagen(datos_imagen, cola_resultado):
    try:
       
        imagen = Image.open(io.BytesIO(datos_imagen))
        imagen_gris = imagen.convert('L')
        buffer = io.BytesIO()
        imagen_gris.save(buffer, format="JPEG")
        resultado = buffer.getvalue() 
        cola_resultado.put(resultado)

    except Exception as e:
        cola_resultado.put(str(e))

    finally:
       
        sem.release()

@app.route('/procesar', methods=['POST'])
def procesar():
    try:
        # Obtener la imagen enviada por el cliente
        datos_imagen = request.files['imagen'].read()
        sem.acquire()
       
        cola_resultado = Queue()
        proceso = Process(target=procesar_imagen, args=(datos_imagen, cola_resultado))
        proceso.start()
        resultado = cola_resultado.get()
        proceso.join()

        if isinstance(resultado, bytes):
            imagen_procesada_base64 = base64.b64encode(resultado).decode()
            return jsonify({"estado": "completado", "imagen_procesada": imagen_procesada_base64})
        else:
            return jsonify({"estado": "error", "mensaje": resultado})

    except Exception as e:
        return jsonify({"estado": "error", "mensaje": str(e)})

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Servidor para procesar imágenes.')
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1', help='Dirección IP de escucha')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Puerto de escucha')
    args = parser.parse_args()

    app.run(host=args.ip, port=args.port, debug=True)
