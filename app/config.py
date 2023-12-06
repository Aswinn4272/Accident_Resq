import os

def generate_secret_key():
    return os.urandom(24).hex()

SECRET_KEY = generate_secret_key()

DEBUG = True
# Other configuration options...
