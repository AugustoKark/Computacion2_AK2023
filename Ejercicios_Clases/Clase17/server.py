# ## EJERCICIOS ##
# 1 - Implementar un servidor http con el módulo http.server que sirva diferentes páginas utilizando como base el código analizado en clase.
# 2- Utilizar links para navegar entre las distintas páginas.

import http.server
import socketserver
import urllib.parse

# GET / HTTP/1.1

PORT = 1111


class handler_manual (http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
              self.path = '/index.html'

        try:
            with open(self.path[1:], 'rb') as file:
                content = file.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            self.send_error(404, 'Archivo no encontrado')
        

    def do_POST(self):
        if self.path == '/submit_form':
            input_data=self.rfile.read(int(self.headers['Content-Length']))
            print("INPUT DATA: ", input_data)
                                    
            response_content = "¡Formulario enviado correctamente!"
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(response_content.encode('utf-8'))
        else:
            self.send_error(404, 'Página no encontrada')   


        
       


socketserver.TCPServer.allow_reuse_address = True

#myhttphandler = http.server.BaseHTTPRequestHandler
#myhttphandler = http.server.SimpleHTTPRequestHandler
myhttphandler = handler_manual


#httpd = socketserver.TCPServer(("", PORT), myhttphandler)
httpd = http.server.HTTPServer(("", PORT), myhttphandler)
#httpd = http.server.ThreadingHTTPServer(("", PORT), myhttphandler)

print(f"Opening httpd server at port {PORT}")

httpd.serve_forever()

httpd.shutdown()