






def encrypt_file (shift1. shift2, input_path: str, output_path: str) -> None:
    with open (input_path, "r", encoding='utf-8') as input_file:
        content = input_file.read()
    




def main():
    shift1_input = int(input("Enter a non-negative integer for shift1: "))
    shift2_input = int(input("Enter a non-negative integer for shift2: "))
    if shift1_input < 0 or shift2_input < 0:
        print ("Error: shifts must be non-negative integer!")
    
    else:
        encrypt_file (shift1_input, shift2_input, "raw_text.txt", "encrypted_text.txt")

        decrypt_file (shift1_input, shift2_input, "encrypted_text.txt", "decrypted_text.txt")

        verify_files (i dont know man)
    
if __name__ == "__main__":
    main()