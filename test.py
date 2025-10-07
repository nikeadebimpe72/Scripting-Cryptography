#!/usr/bin/env python3


def get_mode():
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if mode in ['e', 'd']:
            return mode
        print("Please enter 'e' for encrypt or 'd' for decrypt.")

def get_rotation():
    while True:
        rotation = input("Enter the rotation amount (1-25): ")
        if rotation.isdigit() and 1 <= int(rotation) <= 25:
            return int(rotation)
        print("Please enter a number between 1 and 25.")
import string
def get_file_name():
    return input("Enter the name of the file to process: ")

def process_text(text, rotation, mode):
    alphabet = string.ascii_letters
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if mode == 'e':
                new_index = (index + rotation) % len(alphabet)
            else:
                new_index = (index - rotation) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using a Caesar Cipher.")
    print()

    mode = get_mode()
    rotation = get_rotation()
    file_name = get_file_name()

    try:
        with open(file_name, 'r') as file:
            original_text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return

    processed_text = process_text(original_text, rotation, mode)

    output_file = f"{'encrypted' if mode == 'e' else 'decrypted'}_{file_name}"
    with open(output_file, 'w') as file:
        file.write(processed_text)

    print("\nResults:")
    print(f"Original file: {original_text}")
    print(f"{'Encryption' if mode == 'e' else 'Decryption'} key: {rotation}")
    print(f"{'Encrypted' if mode == 'e' else 'Decrypted'} file: {processed_text}")
    print(f"Output saved to: {output_file}")

    print("\nNote: To decrypt, use the same rotation number used for encryption.")
    print("Remember to take a screenshot of this output and save it as mrot13.png")

if __name__ == "__main__":
    main()
