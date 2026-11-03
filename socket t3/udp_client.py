import socket

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

# Inisialisasi socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pesan = b"Halo Server, ini pesan cepat via UDP!"

# Langsung kirim tanpa perlu connect terlebih dahulu
client_socket.sendto(pesan, (TARGET_IP, TARGET_PORT))
print("[*] Paket UDP berhasil ditembakkan ke server.")

# Menunggu balasan dari server (maksimal 1024 bytes)
data_balasan, server_address = client_socket.recvfrom(1024)
print(f"[Balasan Server UDP]: {data_balasan.decode('utf-8')}")

client_socket.close()