import random
import string

class Shortener:
    token_size = 5

    def __init__(self, token_size=5):
        self.token_size = token_size

    def generate_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(self.token_size))