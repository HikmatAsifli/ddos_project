from random import randint

def random_ip():
    return f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"
