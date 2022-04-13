import socket

target_host= "127.0.0.1"

target_port = 80

# creating socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sending dummy data
client.sendto(b"This is a sample data",(target_host,target_port))

# reciving data

data, address = client.recvfrom(4096)






print(data)