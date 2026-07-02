import string
import random

BASE62_ALPHABET = string.digits + string.ascii_letters


def generate_random_short_id(length: int = 6) -> str:
    return "".join(random.choices(BASE62_ALPHABET, k=length))
