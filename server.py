import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.MSG_LENGTH = 1024

    def start(self):
        self.server_socket.bind((self.host, self.port))
        print(f"[SERVER] listening to new connections...")
        self.server_socket.listen()
        conn, addr = self.server_socket.accept()
        with conn:
            print(f"[SERVER] Connected to {addr}")
            while True:
                conn.sendall(b"Hello from server.")
                data = conn.recv(self.MSG_LENGTH)
                if not data:
                    break
                print(f"[SERVER] Received from client: {data.decode()}")
                break

    def stop(self):
        self.server_socket.close()

def main():
    HOST = "127.0.0.1"
    PORT = 8081
    server = Server(HOST, PORT)
    server.start()
    server.stop()

if __name__ == "__main__":
    main()