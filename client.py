import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.MSG_LENGTH = 1024

    def start(self):
        self.client_socket.connect((self.host, self.port))
        while True:
            data = self.client_socket.recv(self.MSG_LENGTH)
            if not data:
                break
            print(f"[CLIENT] Received from server: {data.decode()}")
            self.send_message("Hello from client.")
            break


    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def stop(self):
        self.client_socket.close()

def main():
    HOST = "127.0.0.1"
    PORT = 8081
    client = Client(HOST, PORT)
    client.start()
    client.stop()

if __name__ == "__main__":
    main()