import socket

server_socket = socket.socket(socket,AF_INET,socket,SOCK_STREAM)

HOST = 'localhost'
PORT = 5000

server_socket.bind((HOST, PORT))

server_socket.listen(1)
print(f"[+] Server berjalan dan menunggu koneksi di (HOST):(PORT)...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"[+] Terhubung dengan client dari: (client_address)")

    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    
    print(f"[Request DIterima] {data}")

    response = data.upper()

    client_socket.send(response.encode('utf-8'))
    print