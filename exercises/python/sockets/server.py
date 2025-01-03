import socket
import threading


class Server:
    def __init__(
        self, server_address: str = "127.0.0.1", server_port: int = 9999
    ) -> None:
        self.server_address = server_address
        self.server_port = server_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.clients = []

    def run_server(self) -> None:
        self.server_socket.listen()
        print(f"Listening on {self.server_address}:{self.server_port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection acceppted from {client_address[0]}:{client_address[1]}")
            client_socket.send(
                "Connection with the server successfully established\n".encode("utf-8")
            )
            client_socket.send("ALIAS".encode("utf-8"))
            alias = client_socket.recv(1024).decode("utf-8")
            print(f"{alias} has joined the chat room.")
            self.clients.append(client_socket)
            self.broadcast(f"{alias} joined the conversation".encode("utf-8"))
            t = threading.Thread(target=self.handle_client, args=(client_socket, alias))
            t.start()

    def broadcast(self, message) -> None:
        for client_socket in self.clients:
            client_socket.send(message)

    def handle_client(self, client_socket, alias: str) -> None:
        while True:
            try:
                message: str = client_socket.recv(1024).decode("utf-8")
                if message.lower() == "!quit":
                    self.clients.remove(client_socket)
                    print(f"{alias} left the chat room.")
                    self.broadcast(f"{alias} left the chat room".encode("utf-8"))
                    break
                message = f"{alias}: {message}".encode("utf-8")
                self.broadcast(message)
            except:
                self.clients.remove(client_socket)
                self.broadcast(
                    f"Connection with {alias} terminated unexpectedly".encode("utf-8")
                )
                break
        client_socket.close()


if __name__ == "__main__":
    server = Server()
    server.run_server()
