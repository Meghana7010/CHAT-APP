import socket
import threading


HOST = 'localhost'
PORT = 12345
LISTNER_LIMIT = 5
active_clients = []

def listen_for_messages(client, username):
    while 1:
        message  = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '-' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message send from client {username} is empty")

def send_message_to_client(client, message):
    client.sendall(message.encode())

def send_messages_to_all(message):
    for user in active_clients: 
       send_message_to_client(user[1], message)


def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER-" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("client username is empty")

    threading.Thread(target= listen_for_messages, args= (client, username, )).start()

#main
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"running on {HOST} and {PORT}")
    except:
        print(f"Unable to bind the host {HOST} and port {PORT}")

        server.listen(LISTNER_LIMIT)

    while 1:
        client, address = server.accept()
        print(f"Successfully conected to {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()

if __name__ == '__main__':
    main()
