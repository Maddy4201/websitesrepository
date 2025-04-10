import random
import string

class DataGenerator:
    @staticmethod
    def generate_full_name():
        first_names = ['John', 'Emma', 'Liam', 'Olivia']
        last_names = ['Smith', 'Johnson', 'Williams']
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    @staticmethod
    def generate_email(full_name):
        name_part = full_name.lower().replace(' ', '.')
        return f"{name_part}{random.randint(100,999)}@example.com"

    @staticmethod
    def generate_password():
        while True:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
            if (any(c.isalpha() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password)):
                return password
