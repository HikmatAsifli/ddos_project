# DDoS Testing Script

This project is a DDoS testing script designed to test the resilience of a web application. It uses Python and various modules to send a high volume of traffic to a target IP and port.

## Features

- **Random IP Spoofing**: Generates random IP addresses to simulate different attackers.
- **Multithreading**: Uses multiple threads to increase the intensity of the attack.
- **Configurable Packet Count**: Allows you to specify how many packets to send.

## Prerequisites

- Python 3.x
- `aiohttp` library

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
