#!/usr/bin/env python3

import os

def enrypt_ascii(i, rot, encrypt=True):
    ascii_num = ord(i)
    if 97 <= ascii_num <= 122 or 65 <= ascii_num <= 90:
        if encrypt:
            if 97 <= ascii_num <= 122:
                new_ascii = ascii_num + rot
                if new_ascii > 122:
                    new_ascii = new_ascii - 26
            elif 65 <= ascii_num <= 90:
                new_ascii = ascii_num + rot
                if new_ascii > 90:
                    new_ascii = new_ascii - 26
        else:
            if 97 <= ascii_num <= 122:
                new_ascii = ascii_num - rot
                if new_ascii < 97:
                    new_ascii = new_ascii + 26
            elif 65 <= ascii_num <= 90:
                new_ascii = ascii_num - rot
                if new_ascii < 65:
                    new_ascii = new_ascii + 26
        return chr(new_ascii)
    else:
        return i

def write_msg():
    message = input("Enter your message: ")
    if len(message) < 20:
        print("Input must not be less than 20 characters")
        return None
    else:
        file_path = "message.txt"
        with open(file_path, 'w') as file:
            file.write(message)
        return file_path

def encrypt_msg(file_path, rot):
    with open(file_path, 'r') as file:
        file_msg = file.read()

    encrypt_mssg = ""
    for i in file_msg:
        encrypt_mssg += enrypt_ascii(i, rot, encrypt=True)
    with open(file_path, 'w') as output:
        output.write(encrypt_mssg)
    return file_msg, encrypt_mssg

def decrypt_msg(file_path, rot):
    with open(file_path, 'r') as file:
        content = file.read()

    decrypt_mssg = ""
    for i in content:
        decrypt_mssg += enrypt_ascii(i, rot, encrypt=False)
    with open(file_path, 'w') as file:
        file.write(decrypt_mssg)
    return content, decrypt_mssg

def main():
    # Step 1: Create or validate the file
    if not os.path.isfile("message.txt"):
        print("File 'message.txt' does not exist. Please enter a message to create it.")
        file_path = write_msg()
        if file_path is None:
            print("No message entered. Exiting.")
            return
    else:
        file_path = "message.txt"
    
    # Step 2: Choose to encrypt or decrypt
    while True:
        choice = input("Enter whether you want to 'encrypt' or 'decrypt': ").strip().lower()
        if choice in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid Input. Please enter either 'encrypt' or 'decrypt'.")

    # Step 3: Enter the number of rotations
    while True:
        rot = input("Enter the number of rotations: ").strip()
        if rot.isdigit():
            rot = int(rot)
            break
        else:
            print("Enter a valid number.")

    # Step 4: Encrypt or decrypt the file content
    if choice == 'encrypt':
        original_msg, encrypted_msg = encrypt_msg(file_path, rot)
        print(f"Original Message: {original_msg}")
        print(f"Encrypted Message: {encrypted_msg}")
    elif choice == 'decrypt':
        encrypted_msg, decrypted_msg = decrypt_msg(file_path, rot)
        print(f"Encrypted Message: {encrypted_msg}")
        print(f"Decrypted Message: {decrypted_msg}")

if __name__ == "__main__":
    main()
