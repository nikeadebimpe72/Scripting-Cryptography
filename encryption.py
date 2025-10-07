#!/usr/bin/env python3

import os

def gen_ascii(char, rot, encrypt = True):
    for char in range:
         ascii = ord(char)
    if 97 <= ascii <= 122 or 65 <= ascii <= 91:
        if 97 <= ascii <= 122:
            if encrypt:
             new_ascii = ascii + rot
             if new_ascii > 122:
                new_ascii = new_ascii - 26
            else: 
                new_ascii = ascii - rot
        elif 65 <= ascii <= 91:
            if encrypt:
                new_ascii = ascii + rot
                if new_ascii > 91:
                   new_ascii = new_ascii - 26
            else:
                new_ascii = ascii - rot
            if new_ascii < 65:
                new_ascii = new_ascii + 26
        return chr(new_ascii)
    else:
        return char
    



def encrypt_msg(file_path, rot):
    with open(file_path, 'r') as file:
        msg = file.read()

    encrypt_content = ""
    for char in msg:
        encrypt_content += gen_ascii(char, rot,encrypt=True) 

        output_file_path = "msg.txt"

        output_file= open(output_file_path,'w')
        wfile = output_file.write()
        encrypt_content += wfile

    return msg, encrypt_content

def decrypt_msg(file_path, rot):
    file = open(file_path,'r')
    msg = file.read()

    decrypt_content = ""
    for char in msg:
        decrypt_content += gen_ascii(char,rot,encrypt=False) 
        output_file_path = "msg.txt"
        output_file= open(output_file_path,'w')
        wfile = output_file.write()
        decrypt_content += wfile

    return msg, decrypt_content

def main():
    choice = ""
    while True:
        action = input("Enter your choice 1.Encrypt  2.Decrypt").strip().lower()
        if action in ['encrypt', 'decrypt']:
            break
        print("Invalid Input. Please enter 'encrypt' or 'decrypt'. ")
    
    while True:
         try:
            rot = int(input("Enter the number of rotation").strip())
            break
         except ValueError:
             print("Please Enter a valid number")

    while True:
        file_path = input("Enter the file path ").strip()
        if os.path.isfile(file_path):
            break
        print("Plese enter valid file_path.")

    if action =='encrpty':
        original_content, processed_content = encrypt_msg(file_path,rot)
        print("origianl content: ")
        print(original_content)
        print("Encrypted Content ")
        print(encrypt_msg)
        print(processed_content)

    if action ==' decrypt':
        original_content, processed_content = decrypt_msg(file_path,rot)
        print("origianl content: ")
        print(original_content)
        print("decrypted Content ")
        print(decrypt_msg)
        print(processed_content)

if __name__ == "__main__":
    main() 





