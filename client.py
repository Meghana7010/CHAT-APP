import socket
import threading

HOST = 'localhost'
PORT = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"successfully connected")
    except:
        print(f"Unable to connect to server {HOST} and {PORT}")

if __name__ == '__main__':
    main()
