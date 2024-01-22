import socket

HEADER = 64
PORT = 5050
SERVER = "localhost"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(msg):
    message = msg.encode()
    msg_length = str(len(message)).encode()
    msg_length += b' ' * (HEADER - len(msg_length))
    client.send(msg_length)
    client.send(message)
    return client.recv(2048).decode()


def close():
    client.close()
