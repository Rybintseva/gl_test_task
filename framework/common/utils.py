import random
import string


def generate_random_string(size):
    return ''.join(random.choices(string.ascii_lowercase, k=size))


def is_dict_in_dict(super_dict, sub_dict):
    return all(item in super_dict.items() for item in sub_dict.items())
