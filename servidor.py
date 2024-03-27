import socket
import threading

class ReservationServer:
    def __init__(self, host, port):
        """
        Inicializa el servidor de reservas.

        Args:
            host (str): El host en el que se ejecutará el servidor.
            port (int): El puerto en el que escuchará el servidor.
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor de reservas escuchando en {self.host}:{self.port}")
        self.clients = []
        self.resources = ["Habitación 1", "Habitación 2", "Habitación 3"]
        self.running = True

    def start(self):
        """
        Inicia el servidor y acepta conexiones entrantes.
        """
        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Conexión desde {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
                self.clients.append(client_socket)
            except KeyboardInterrupt:
                self.stop()

    def stop(self):
        """
        Detiene el servidor y cierra todas las conexiones de clientes.
        """

        self.running = False
        print("Deteniendo el servidor...")
        for client in self.clients:
            client.close()
        self.server_socket.close()
        print("Servidor detenido.")

    def handle_client(self, client_socket):
        """
        Maneja las solicitudes de un cliente específico.

        Args:
            client_socket (socket.socket): El socket del cliente.
        """
        try:
            while self.running:
                data = client_socket.recv(1024).decode()
                if not data:
                    break

                command, *args = data.split()
                if command == "RESERVAR":
                    resource = args[0] +" "+ args[1]
                    if resource in self.resources:
                        self.resources.remove(resource)
                        client_socket.sendall(f"Reserva exitosa: {resource}".encode())
                    else:
                        client_socket.sendall("Recurso no disponible".encode())

                elif command == "CANCELAR":
                    resource = args[0] +" "+ args[1]
                    if resource not in self.resources:
                        self.resources.append(resource)
                        client_socket.sendall(f"Reserva cancelada: {resource}".encode())
                    else:
                        client_socket.sendall("No hay una reserva para ese recurso".encode())

                elif command == "LISTAR":
                    resources_str = "\n".join(self.resources)
                    client_socket.sendall(f"Recursos disponibles:\n{resources_str}".encode())

        except Exception as e:
            print(f"Error: {e}")

        finally:
            client_socket.close()
            self.clients.remove(client_socket)

if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345
    server = ReservationServer(host, port)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()