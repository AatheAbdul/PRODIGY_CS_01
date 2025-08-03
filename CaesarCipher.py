#Caesar Cipher Encryption and Decryption

#Encryption
def encrypt(plain_text,key):
    encrypted_text=""
    for char in plain_text:
        if char.islower():
            encrypted_text+= chr((ord(char)-ord("a")+key)%26+ord("a"))
        elif char.isupper():
            encrypted_text+= chr((ord(char)-ord("A")+key)%26+ord("A"))
        else:
            encrypted_text+=char
    return encrypted_text

#Decryption
def decrypt(cipher_text,key):
    decrypted_text=""
    for char in cipher_text:
        if char.islower():
            decrypted_text+=chr((ord(char)-ord("a")-key)%26+ord("a"))
        elif char.isupper():
            decrypted_text+=chr((ord(char)-ord("A")-key)%26+ord("A"))
        else:
            decrypted_text+=char
    return decrypted_text

#Validate Key value
def validate_key():
    while True:
        try:
            key = int(input("Enter the key: ")) % 26
            return key
        except ValueError:
            print("Enter valid key")
            continue
#Menu for user input
while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("0. Exit")
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Enter valid choice.")
        continue
    if choice==1:
        print("\n--Encryption--")
        plaintext=input("Enter the plaintext to be encrypted: ")
        key=validate_key()
        print("The encrypted text: ",encrypt(plaintext,key))
    elif choice==2:
        print("\n--Decryption--")
        ciphertext=input("Enter the ciphertext to be decrypted: ")
        key=validate_key()
        print("The decrypted text: ",decrypt(ciphertext,key))
    elif choice==0:
        break
    else:
        print("Enter correct choice.")