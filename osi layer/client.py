import socket

def client_program():
    host = '127.0.0.1'  # Alamat IP lokal (Network Layer - Layer 3)
    port = 5000         # Nomor Port Aplikasi (Transport Layer - Layer 4)

    # 1. MENGINISIASI KONEKSI (Session Layer - Layer 5)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(True, f"[LAYER 5] Sesi terkoneksi ke Server {host}:{port}")

    # 2. MEMBUAT DATA (Application Layer - Layer 7)
    pesan_mentah = "Halo PAK wahyudi, ini pesan rahasia dari Kelompok Rehan!"
    print(f"[LAYER 7] Data dibuat: '{pesan_mentah}'")

    # 3. FORMAT & ENKRIPSI DATA (Presentation Layer - Layer 6)
    # Kita ubah teks string biasa menjadi format bytes (Biner/Bit)
    data_terenkapsulasi = pesan_mentah.encode('utf-8')
    print(f"[LAYER 6] Data diubah ke format Bytes/Biner untuk siap kirim.")

    # 4. PROSES PENGIRIMAN (Transport -> Network -> Data Link -> Physical)
    # Fungsi .send() memicu sistem operasi untuk memecah data menjadi segmen (L4),
    # paket IP (L3), frame (L2), dan aliran listrik/bit (L1) melalui kabel.
    print(f"[OSI ALUR] Mengirimkan data (Proses Enkapsulasi berlangsung...)\n")
    client_socket.send(data_terenkapsulasi)

    # Tutup koneksi
    client_socket.close()
    print("[LAYER 5] Sesi komunikasi ditutup.")

if __name__ == '__main__':
    client_program()