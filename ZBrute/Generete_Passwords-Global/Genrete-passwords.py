import itertools
import string

def password_generator(length_range, file_name):
    with open(file_name, 'w') as file:
        for length in range(*length_range):
            for password_chars in itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=length):
                password = ''.join(password_chars)
                file.write(f"{password}\n")

# Example usage:
password_generator(range(8, 10), "passwords.txt")