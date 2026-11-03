import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class UDPClient {
    public static void main(String[] args) {
        String serverHost = "localhost";
        int serverPort = 5000;

        try (DatagramSocket clientSocket = new DatagramSocket();
                Scanner scanner = new Scanner(System.in)) {

            InetAddress serverAddress = InetAddress.getByName(serverHost);
            System.out.println("=== Terhubung ke UDP Echo Server ===");
            System.out.println("Ketik pesan Anda (ketik 'EXIT' untuk keluar):");

            while (true) {
                System.out.print("> ");
                String inputMessage = scanner.nextLine();

                // Konversi & Kirim ke Server
                byte[] sendBuffer = inputMessage.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(
                        sendBuffer,
                        sendBuffer.length,
                        serverAddress,
                        serverPort);
                clientSocket.send(sendPacket);

                // Jika pengguna ketik EXIT, hentikan perulangan client
                if (inputMessage.equalsIgnoreCase("EXIT")) {
                    System.out.println("Koneksi ditutup.");
                    break;
                }

                // Menunggu dan menerima balasan (Uppercase) dari Server
                byte[] receiveBuffer = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                clientSocket.receive(receivePacket);

                String replyMessage = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Balasan Server (Capital): " + replyMessage);
            }

        } catch (Exception e) {
            System.err.println("Terjadi kesalahan pada Client: " + e.getMessage());
        }
    }
}