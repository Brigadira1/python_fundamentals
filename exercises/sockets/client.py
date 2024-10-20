import socket
import threading


class Client:
    def __init__(
        self, server_address: str = "127.0.0.1", server_port: int = 9999
    ) -> None:
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_address, server_port))

    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message == "ALIAS:":
                    alias = input("Enter your alias: ")
                    self.client_socket.send(alias.encode("utf-8"))
                print(message)
            except Exception as e:
                print("Connection is dropped from server side")
                self.client_socket.close()
                break

    def send(self):
        while True:
            try:
                self.client_socket.send(f"{input()}".encode("utf-8"))
            except Exception as e:
                print("Error communicating with the server")
                self.client_socket.close()
                break


if __name__ == "__main__":
    client = Client()
    receive_thread = threading.Thread(target=client.receive, args=())
    sending_thread = threading.Thread(target=client.send, args=())

    receive_thread.start()
    sending_thread.start()
