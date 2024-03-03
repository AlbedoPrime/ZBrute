import itertools
import string
import os

def password_generator(length_range, base_file_name):
    file_number = 0
    file_name = base_file_name + str(file_number) + ".txt"

    while os.path.getsize(file_name) > 10485760:  # 10 MB threshold
        file_number += 1
        file_name = base_file_name + str(file_number) + ".txt"

    with open(file_name, 'w') as file:
        for length in range(*length_range):
            for password_chars in itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=length):
                password = ''.join(password_chars)
                file.write(f"{password}\n")

                if file.tell() > 30048576000:  # 10 MB threshold
                    file.close()
                    file_number += 1
                    file_name = base_file_name + str(file_number) + ".txt"
                    with open(file_name, 'w') as new_file:
                        with open(file_name.replace(f"{file_number - 1}", f"{file_number}")) as old_file:
                            new_file.write(old_file.read())
                    file = new_file
                    new_file.close()

# Example usage:
password_generator(range(9, 11), "passwords")