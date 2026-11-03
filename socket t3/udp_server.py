import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

balasan = b"Paket UDP kamu sudah sampai di server!"

# SOCK_DGRAM menandakan bahwa kita menggunakan protokol UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"[*] UDP Server siap menerima paket di {UDP_IP}:{UDP_PORT}...")

while True:
    # recvfrom() mengembalikan data SEKALIGUS alamat IP si pengirim
    data, address = server_socket.recvfrom(1024)
    print(f"[+] Menerima paket UDP dari {address}: {data.decode('utf-8')}")
    
    # Mengirim balasan langsung ke alamat pengirim
    server_socket.sendto(balasan, address)