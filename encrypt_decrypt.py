def encrypt(text, shift):
    encrypt = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                code = ord('A')
            else:
                code = ord('a')
            
            char_position = ord(char) - code
            new_position = (char_position + shift) % 26
            shifted_char = chr(code + new_position)
            encrypt += shifted_char
        else:
            encrypt += char
    return encrypt

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("caesar cipher encryption and decryption program")
    message = input("enter the meassage you want to encrypt and decrypt")
    while True:
        try:
            shift = int(input("enter the number of shift value: "))
            break
        except ValueError:
            print("please enter a valid integer: ")

    encryption_message = encrypt(message, shift)
    decryption_message = decrypt(encryption_message, shift)

    print("your message is:", message)
    print("encryption message is:", encryption_message)
    print("decryption message is:", decryption_message)

if __name__ == "__main__":
    main()
