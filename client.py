import socket
import sys
import json
import os
import linux,subprocess
HOST, PORT = "localhost", 4000
def client_program(): host = socket.gethostname() 
port = 4000 
client_socket =
socket.socket() 
client_socket.connect((host, port))
#m ='{"id": 2, "name": "abc"}
m = {"id": 2, "name": "abc"} 
message = input(" -> ") 
while message.lower().strip() != 'bye': client_socket.send(message.encode()) 
data =
client_socket.recv(1024).decode() 
if __name__ == '__main__': 
client_program()
