import random
import string

def generate_email():
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{prefix}@{domain}.ru"