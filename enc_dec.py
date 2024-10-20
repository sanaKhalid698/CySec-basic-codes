'''Objective: Implement a basic Caesar Cipher to encrypt and decrypt messages.
Requirements:
Ask the user for a message and a shift value.
Provide functions to encrypt and decrypt the message using the Caesar Cipher technique.'''
def encryption(message: str, shift_value:int):
    encrypted_msg:str=""
    for char in message:
        if char.islower():
            encrypted_msg+=chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
        elif char.isupper():
            encrypted_msg+=chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
        else:
            encrypted_msg+=char  
    print(f"Encrypted message {encrypted_msg}")

def decryption(message: str, shift_value:int):
    decrypted_msg:str=""
    for char in message:
        if char.islower():
            decrypted_msg+=chr((ord(char) - ord('a') - shift_value) % 26 + ord('a'))
        elif char.isupper():
            decrypted_msg+=chr((ord(char) - ord('A') - shift_value) % 26 + ord('A'))
        else:
            decrypted_msg+=char   
    print(f"Decrypted message {decrypted_msg}")

if __name__ == "__main__":
    message: str = input("Enter the message:")
    shift_value: int = int(input("Enter the shift value:"))
    choice: int= int(input("Press 1 for encryption , Press 2 for decryption "))
    if choice == 1: encryption(message, shift_value)
    elif choice == 2: decryption (message, shift_value)
    else: print("wrong choice")
