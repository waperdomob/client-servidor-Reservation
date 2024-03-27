import socket

class ReservationClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Conectado al servidor de reservas en {self.host}:{self.port}")

    def send_command(self, command):
        self.client_socket.sendall(command.encode())
        data = self.client_socket.recv(1024).decode()
        print(data)

if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345
    client = ReservationClient(host, port)

    while True:
        command = input("Ingrese un comando (RESERVAR <recurso>, CANCELAR <recurso>, LISTAR): ")
        if command.upper() == "SALIR":
            break
        
        client.send_command(command)

    client.client_socket.close()