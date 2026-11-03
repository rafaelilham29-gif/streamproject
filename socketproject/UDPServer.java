import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPServer {
    public static void main(String[] args) {
        int port = 5000;

        try (DatagramSocket serverSocket = new DatagramSocket(port)) {
            System.out.println("UDP Echo-Server (Uppercase) siap di port " + port + "...");

            byte[] receiveBuffer = new byte[1024];

            while (true) {
                // 1. Terima paket dari client
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                serverSocket.receive(receivePacket);

                String message = new String(receivePacket.getData(), 0, receivePacket.getLength());

                // Ambil alamat IP dan Port client asal
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();

                System.out.println("[" + clientAddress.getHostAddress() + ":" + clientPort + "] Terima: " + message);

                // Jika client minta EXIT, server cukup cetak info (server tetap jalan)
                if (message.equalsIgnoreCase("EXIT")) {
                    System.out.println(
                            "Client [" + clientAddress.getHostAddress() + ":" + clientPort + "] telah keluar.");
                    continue;
                }

                // 2. Ubah teks menjadi HURUF KAPITAL
                String uppercaseMessage = message.toUpperCase();
                byte[] sendBuffer = uppercaseMessage.getBytes();

                // 3. Kirim balik (reply) ke Client
                DatagramPacket sendPacket = new DatagramPacket(
                        sendBuffer,
                        sendBuffer.length,
                        clientAddress,
                        clientPort);
                serverSocket.send(sendPacket);

                // Reset buffer
                receiveBuffer = new byte[1024];
            }
        } catch (Exception e) {
            System.err.println("Terjadi kesalahan pada Server: " + e.getMessage());
        }
    }
}