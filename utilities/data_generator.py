import json
import os
import random
import string

first_names = ["Scott", "Jack", "George", "Miles", "Harry", "Oliver"]
last_names = ["Jones", "Smith", "Taylor", "Brown", "Robinson", "Lewis"]

def get_random_first_name():
    return random.choice(first_names)

def get_random_last_name():
    return random.choice(last_names)

def generate_email(first_name):
    suffix = ''.join(random.choices(string.digits, k=3))
    return f"{first_name.lower()}{suffix}@yopmail.com"

def get_random_website_name():
    website_name_first = ["testuser", "useroftest", "testofwebsite", "testwebistenumber"]
    website_second_name = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_part = random.choice(website_name_first)
    second_part = random.choice(website_second_name)
    return first_part + second_part


def generate_phone_number():
    # Generates a 10-digit Indian phone number starting with 7, 8, or 9
    start_digit = random.choice(["7", "8", "9"])
    remaining_digits = ''.join(random.choices(string.digits, k=8))
    return start_digit + remaining_digits


