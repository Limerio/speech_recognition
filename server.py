import os
import socket
import threading

from utils.assistant import BasicAssistant

done = False

model_name = "data/sarah"

# socket
HEADER = 64
PORT = 5050
SERVER = "localhost"

assistant = BasicAssistant('data/intents.json', model_name=model_name)

if os.path.exists(f'{model_name}.keras'):
    assistant.load_model()
else:
    assistant.fit_model(epochs=50)
    assistant.save_model()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def handle_task(conn: socket.socket, text: str) -> None:
    print("Task started")
    category, response = assistant.process_input(text)

    args = text.split(' ')

    try:
        task = __import__("tasks.%s" % category, fromlist=["tasks"])
        msg = task.run(args, response)
        msg.strip()
        conn.send(msg.encode())
        print("Task finished")
    except ImportError:
        print("Error to find the task")


def handle_client(conn: socket.socket) -> None:
    connected = True
    print("User connected")
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode()
            if msg.lower() == 'disconnect':
                conn.send("Disconnected".encode())
                connected = False
                break

            handle_task(conn, msg)

    conn.close()


print("Server is starting....")
server.listen()
print('Server started')
while not done:
    try:
        conn, _addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()
    except KeyboardInterrupt:
        print("Stopped")
        done = True

server.close()
