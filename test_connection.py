import socket
import time

ip = "192.168.137.1"
port = 5050

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, port))

def send(msg):
    try:
        message = msg.encode('utf-8')
        socket.send(message)
    except socket.error as e:
        print(e)

send('Hello World')
time.sleep(0.001)
send('Hello Bam')
input()
send('disconnect')
