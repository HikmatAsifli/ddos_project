import unittest
from src.utils.ip_utils import generate_private_ip
from src.utils.attack import send_packet

class TestAttack(unittest.TestCase):
    def test_generate_private_ip(self):
        ip = generate_private_ip()
        self.assertIsInstance(ip, str)
        self.assertEqual(len(ip.split('.')), 4)

    def test_send_packet(self):
        try:
            send_packet("127.0.0.1", 80, "192.168.1.1")
        except Exception as e:
            self.fail(f"send_packet raised an exception: {e}")

    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            send_packet("999.999.999.999", 80, "192.168.1.1")

if __name__ == '__main__':
    unittest.main()
