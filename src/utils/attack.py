import socket
import struct

def send_packet(target_ip, target_port, spoofed_ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = struct.pack("!4s", bytes(spoofed_ip, 'utf-8'))
        sock.sendto(payload, (target_ip, target_port))
    except Exception as e:
        print(f"Error sending packet: {e}")
