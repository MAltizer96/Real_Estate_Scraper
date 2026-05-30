from time import time


def get_random_delay():
    return 1 + (2 * time.random())