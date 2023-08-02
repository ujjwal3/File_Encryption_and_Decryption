import re
import os


def encript(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("A") if char.isupper() else ord("a")

            # ord of letter  - ascii_offset of capital is 65(A) to 90(Z) + key 1 to 25 any integer if total of this is > 26
            # then divide by 26 and its remainder + ascii_offset of capital is 65,
            # the result of this, is the position of alphabet (0 to 25)

            # ord of letter  - ascii_offset of small is 97(a) to 122(z) + key 1 to 25 any integer if total of this is < 26
            # then this total is the position of alphabet (0 to 25)
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


print("Welcome to File Encryption and Decryption!")
print("1. Encrypt a file")
print("2. Decrypt a file")


user_input = int(input("Choose an option: "))
while user_input != 1 and user_input != 2:
    print("INVALID INPUT")
    print("Welcome to File Encryption and Decryption!")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    user_input = int(input("Choose an option: "))

if user_input == 1:
    input_path = input("Enter the path of the input file: ")
    from os.path import exists

    while not os.path.exists(input_path):
        print("File does't not exist")
        input_path = input("Enter the path of the input file: ")
    output_path = input("Enter the path of the output file: ")
    encription_key = int(
        input("Enter the encryption key (a number between 1 and 25): ")
    )

    with open(input_path, "r") as input_file:
        content = input_file.read()

    encripted_content = encript(content, encription_key)
    full_stop = encripted_content.replace(".", "#%&")
    coma = full_stop.replace(",", "%+@")
    space = coma.replace(" ", "@#$")

    with open(output_path, "w") as output_file:
        output_file.write(space)
        print(
            f"File '{input_path}' encrypted successfully and saved as '{output_path}'."
        )


elif user_input == 2:
    inputFilepath = input("Enter the path of the input file: ")
    from os.path import exists

    while not os.path.exists(inputFilepath):
        print("File does't not exist")
        inputFilepath = input("Enter the path of the input file: ")
    outputFilepath = input("Enter the path of the output file: ")
    encription_key = int(
        input("Enter the encryption key (a number between 1 and 25): ")
    )

    with open(inputFilepath, "r") as input_file:
        content = input_file.read()

    decripted_content = encript(content, -encription_key)
    full_stop = decripted_content.replace("#%&", ".")
    coma = full_stop.replace("%+@", ",")
    space = coma.replace("@#$", " ")

    with open(outputFilepath, "w") as output_file:
        output_file.write(space)
        print(
            f"File '{inputFilepath}' decripted successfully and saved as '{outputFilepath}'."
        )
