from random import randint

def generate_private_ip():
    # Generate a random IP in private ranges
    first_octet = randint(10, 10)
    second_octet = randint(0, 255)
    third_octet = randint(0, 255)
    fourth_octet = randint(1, 255)
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
