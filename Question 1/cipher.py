import os 

def transform_char (char, shift1, shift2, decrypt = False):
     """
    Transform a single character using the assignment's encryption rules.
    - a-n: shift forward by shift1 * shift2 (14 letters)
    - o-z: shift backward by shift1 + shift2 (12 letters)
    - A-M: shift backward by shift1 (13 letters)
    - N-Z: shift forward by shift2 * shift2 (13 letters)
    - 0-9: shift by shift1 - shift2 (10 digits)
    - Other chars (space, punctuation, etc) stay unchanged.
    If decrypt=True, reverse the operation.
    """
    if "a" <= char <= "z":
        # Case 1: a to n (first 14 letters)
        if "a" <= char <= "n":
            position = ord (char) - ord ('a')
            if decrypt == False: 
                encrypted_position = (position + shift1 * shift2) % 14
            else: 
                encrypted_position = (position - shift1 * shift2) % 14       
            encrypted_char = chr (encrypted_position + ord ('a'))
        
        else: # Case 2: o to z (last 12 letters)
            position = ord (char) - ord ('o')
            if decrypt == False: 
                encrypted_position = (position - (shift1 + shift2)) % 12
            else: 
                encrypted_position = (position + (shift1 + shift2)) % 12
            encrypted_char = chr (encrypted_position + ord ('o'))

    elif "A" <= char <= "Z":
        # Case 3: A to M (first 13 letters)
        if "A" <= char <= "M":
            position = ord (char) - ord ('A')
            if decrypt == False: 
                encrypted_position = (position - shift1) % 13
            else: 
                encrypted_position = (position + shift1) % 13
            encrypted_char = chr (encrypted_position + ord ('A'))
        else: # Case 4: N to Z (last 13 letters)
            position = ord (char) - ord ('N')
            if decrypt == False: 
                encrypted_position = (position + shift2 * shift2) % 13
            else:
                encrypted_position = (position - shift2 * shift2) % 13
            encrypted_char = chr (encrypted_position + ord ('N'))
    # Case 5: Numbers 0-9
    elif "0" <= char <= "9":
        position = ord (char) - ord ('0')
        if decrypt == False: # Encrypt
            encrypted_position = (position + (shift1 - shift2)) % 10
        else:
            encrypted_position = (position - (shift1 - shift2)) % 10
        encrypted_char = chr (encrypted_position + ord ('0'))
    
    else: # No change for spaces, tabs, newlines, punctuation, symbols
        encrypted_char = char
    
    return encrypted_char


def encrypt_file (shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    # Read input file, encrypt each character, and write to output file.
    with open (input_path, "r") as input_file:
        content = input_file.read()

    # Encrypt char by char
    encrypted_characters = ""
    for char in content:
        transformed = transform_char (char, shift1, shift2)
        encrypted_characters += transformed

    # Write encrypted result
    with open (output_path, "w") as output_file:
        output_file.write (encrypted_characters)

def decrypt_file (shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    # Read encrypted file, decrypt each character, and write to decrypted file.
    with open (input_path, "r") as input_file:
        content = input_file.read()
    decrypted_characters = ""
    for char in content:
        # Use decrypt=True to reverse the shift
        transformed = transform_char (char, shift1, shift2, decrypt = True)
        decrypted_characters += transformed

    with open (output_path, "w") as output_file:
        output_file.write(decrypted_characters)
        
def verify_files (file1_path: str, file2_path: str):
    # Compare two files to check if decryption returned the original text.
    with open (file1_path, "r") as file1:
        content1 = file1.read()
    with open (file2_path, "r") as file2:
        content2 = file2.read()
    if content1 == content2:
        print ("Verification successful: The files are identical.")
    else:
        print ("Verification failed: The files are different.")
        

def main():
    # Main program: get shifts, handle file paths, run encrypt/decrypt/verify.
    shift1_input = int(input("Enter a non-negative integer for shift1: "))
    shift2_input = int(input("Enter a non-negative integer for shift2: "))

    # Use absolute path so it works even if terminal is in different folder
    base_dir = os.path.dirname (os.path.abspath(__file__))
    raw_file = os.path.join(base_dir, "raw_text.txt")
    encrypted_file = os.path.join(base_dir, "encrypted_text.txt")
    decrypted_file = os.path.join(base_dir, "decrypted_text.txt")
 
    # Validate shifts must be >= 0
    if shift1_input < 0 or shift2_input < 0:
        print ("Error: shifts must be non-negative integer!")
    
    else:
        encrypt_file (shift1_input, shift2_input, raw_file, encrypted_file)
        print ("Encryption complete")

        decrypt_file (shift1_input, shift2_input, encrypted_file, decrypted_file)
        print ("Decryption complete")

        verify_files (raw_file, decrypted_file)
    
if __name__ == "__main__":
    main() 