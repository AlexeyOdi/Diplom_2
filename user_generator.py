import random
import string

def generate_user():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    test_data = {}

    test_data['email'] = generate_random_string(10)+'@yandex.ru'
    test_data['password'] = generate_random_string(10)
    test_data['name'] = generate_random_string(10)

    return test_data

def generate_email():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    return generate_random_string(10)+'@yandex.ru'