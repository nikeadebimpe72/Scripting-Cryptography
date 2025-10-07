#!/urs/bin/py

#creating ascii table with rot 16

message = input("Enter the encrypted or decrpted message")
final = ""

for i in message:
    ascii = ord(i)
    if 97 <= ascii <= 122 or 65 <= ascii <= 91:
        if 97 <= ascii <= 122:
            new_ascii = ascii + 13
            if new_ascii > 122:
                new_ascii = new_ascii - 26
        if 65 <= ascii <= 91:
            new_ascii = ascii + 13
            if new_ascii > 91:
                new_ascii = new_ascii - 26
        final += chr(new_ascii)
    else:
        final += chr(ascii)
print(final)