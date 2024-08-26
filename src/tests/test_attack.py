import unittest
from src.utils.ip_utils import random_ip
from src.utils.attack import send_packet

class TestAttack(unittest.TestCase):
    def test_random_ip(self):
        ip = random_ip()
        self.assertIsInstance(ip, str)
        self.assertEqual(len(ip.split('.')), 4)

    def test_send_packet(self):
        try:
            send_packet("127.0.0.1", 80, "192.168.1.1")
        except Exception as e:
            self.fail(f"send_packet raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
