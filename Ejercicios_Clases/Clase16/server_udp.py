import threading
import socketserver



def encrypt_rot13(msg):
        while True: 
            for char in msg:
                if char.isalpha():
                    if char.islower():
                        encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
                    else:
                        encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
                    encrypted_text += encrypted_char
                else:
                    encrypted_text += char
            
            return(encrypted_char)  


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
            # data = self.request[0].strip()
            # socket = self.request[1]
            # current_thread = threading.current_thread()
            data = self.request.recv(1024).strip()
            response=encrypt_rot13(data)
            socket = self.request
            print("cliente: {}, escribió: {}".format( self.client_address, response))
            socket.sendto(data.upper(), self.client_address)



if __name__ == "__main__":

    HOST, PORT = "localhost", 50002
    with socketserver.ThreadingUDPServer((HOST, PORT), ThreadedUDPRequestHandler) as server:
    
        print("Servidor corriendo en la ip {} y puerto {}".format(HOST, PORT))
        server.serve_forever()

# class MyUDPHandler(socketserver.BaseRequestHandler):
#  

#     def handle(self):
#         data = self.request[0].strip()
#         socket = self.request[1]
#         print("{} wrote:".format(self.client_address[0]))
#         print(data)
#         socket.sendto(data.upper(), self.client_address)
#         time.sleep(20)
        

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
#         server.serve_forever()
