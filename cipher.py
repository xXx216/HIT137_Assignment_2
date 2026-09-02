import os 

def transform_char (char, shift1, shift2, decrypt = False):
    # Checking if character is lower, upper letter, or a number.
    if "a" <= char <= "z":
        if "a" <= char <= "n":
            position = ord (char) - ord ('a')
            if decrypt == False: # Encrypt
                encrypted_position = (position + shift1 * shift2) % 14
            else: # Decrypt (flip + to -)
                encrypted_position = (position - shift1 * shift2) % 14       
            encrypted_char = chr (encrypted_position + ord ('a'))
        
        else: # o - z
            position = ord (char) - ord ('o')
            if decrypt == False: # Encrypt
                encrypted_position = (position - (shift1 + shift2)) % 12
            else: # Decrypt (flip + to -)
                encrypted_position = (position + (shift1 + shift2)) % 12
            encrypted_char = chr (encrypted_position + ord ('o'))

    elif "A" <= char <= "Z":
        if "A" <= char <= "M":
            position = ord (char) - ord ('A')
            if decrypt == False: # Encrypt
                encrypted_position = (position - shift1) % 13
            else: 
                encrypted_position = (position + shift1) % 13
            encrypted_char = chr (encrypted_position + ord ('A'))
        else: # N - Z
            position = ord (char) - ord ('N')
            if decrypt == False: # Encrypt
                encrypted_position = (position + shift2 * shift2) % 13
            else:
                encrypted_position = (position - shift2 * shift2) % 13
            encrypted_char = chr (encrypted_position + ord ('N'))
    
    elif "0" <= char <= "9":
        position = ord (char) - ord ('0')
        if decrypt == False: # Encrypt
            encrypted_position = (position + (shift1 - shift2)) % 10
        else:
            encrypted_position = (position - (shift1 - shift2)) % 10
        encrypted_char = chr (encrypted_position + ord ('0'))
    
    else: # char is Spaces, tabs, newlines, punctuation, symbols, so unchanged.
        encrypted_char = char
    
    return encrypted_char


def encrypt_file (shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    with open (input_path, "r") as input_file:
        content = input_file.read()

    encrypted_characters = ""
    for char in content:
        transformed = transform_char (char, shift1, shift2)
        encrypted_characters += transformed

    with open (output_path, "w") as output_file:
        output_file.write (encrypted_characters)

#-------
def decrypt_file (shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    with open (input_path, "r") as input_file:
        content = input_file.read()
    decrypted_characters = ""
    for char in content:
        transformed = transform_char (char, shift1, shift2, decrypt = True)
        decrypted_characters += transformed
    with open (output_path, "w") as output_file:
        output_file.write(decrypted_characters)
        



#-------
def verify_files (file1_path: str, file2_path: str):
    with open (file1_path, "r") as file1:
        content1 = file1.read()
    with open (file2_path, "r") as file2:
        content2 = file2.read()
    if content1 == content2:
        print ("Verification successful: The files are identical.")
    else:
        print ("Verification failed: The files are different.")
        

def main():
    shift1_input = int(input("Enter a non-negative integer for shift1: "))
    shift2_input = int(input("Enter a non-negative integer for shift2: "))
    if shift1_input < 0 or shift2_input < 0:
        print ("Error: shifts must be non-negative integer!")
    
    else:
        encrypt_file (shift1_input, shift2_input, "raw_text.txt", "encrypted_text.txt")
        print ("Encryption complete")

        
        decrypt_file (shift1_input, shift2_input, "encrypted_text.txt", "decrypted_text.txt")
        print ("Decryption complete")

        verify_files ("raw_text.txt", "decrypted_text.txt")
    
if __name__ == "__main__":
    main() 