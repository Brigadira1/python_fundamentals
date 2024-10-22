import socket
import sys
import threading


class Client:
    def __init__(
        self, server_address: str = "127.0.0.1", server_port: int = 9999
    ) -> None:
        self.client_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_address, server_port))
        self.alias = None

    def receive(self, event) -> None:
        while True:
            try:
                message: str = self.client_socket.recv(1024).decode("utf-8")
                # print(f"Raw message received: {repr(message)}")
                if "ALIAS" in message:
                    al = input("Enter your alias: ")
                    self.alias = al
                    self.client_socket.send(self.alias.encode("utf-8"))
                    event.set()
                else:
                    # event.set()
                    print(message)
            except Exception() as e:
                print(f"Connection is dropped from server side: {e}")
                break
        self.client_socket.close()
        sys.exit(0)

    def send(self, event) -> None:
        event.wait()
        while True:
            try:
                message: str = str(input())
                self.client_socket.send(f"{message}".encode("utf-8"))
            except Exception() as e:
                print(f"Error communicating with the server: {e}")
                break
        self.client_socket.close()
        sys.exit(0)


if __name__ == "__main__":
    client = Client()

    event = threading.Event()
    receive_thread = threading.Thread(target=client.receive, args=(event,))
    receive_thread.start()
    sending_thread = threading.Thread(target=client.send, args=(event,))
    sending_thread.start()
