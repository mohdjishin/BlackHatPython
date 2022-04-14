from cgitb import handler
import socket
import threading


IP = '0.0.0.0'
port= 80

def main():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 1 server start listen
    server.bind((IP,port))
    
    #number of connection allowed
    server.listen(5)
    
    print(f'[+] Listening on {IP}:{port}...')
    
    while True:
        client,address =server.accept()
        
        #address[0] = ip
        #address[1] = port 
        print(f'[+] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'Sample Server response!!!')
        
        
if __name__ == '__main__':
    main()                                                                                                                                          
