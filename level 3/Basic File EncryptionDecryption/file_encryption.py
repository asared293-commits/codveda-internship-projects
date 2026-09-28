'''

Description: Create a Python script that encrypts and
decrypts text files using a simple encryption
algorithm (e.g., Caesar cipher or Fernet encryption).
Task 2: 
Basic File Encryption/Decryption
Allow the user to input a file for encryption or
decryption.
Encrypt the file content and save it as a new file.
Provide functionality to decrypt the file back to its
original form

'''
import os

def encrypt_text(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr(
                (ord(char) - shift_base + shift) % 26 + shift_base
            )
        else:
            encrypted_text += char
    return encrypted_text


def decrypt_text(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr(
                (ord(char) - shift_base - shift) % 26 + shift_base
            )
        else:
            decrypted_text += char
    return decrypted_text


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


def main():

    print("FILE ENCRYPTION/DECRYPTION")
    print("What do you want to do?")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '3':
        print("Exiting the program.")
        return

    file_name = input("Enter the file name: ").strip()
    shift = int(input("Enter the shift value for encryption/decryption: "))

    # Get the folder and just the file name
    folder = os.path.dirname(file_name)
    original_name = os.path.basename(file_name)

    if choice == '1':
        content = read_file(file_name)
        encrypted_content = encrypt_text(content, shift)

        new_file_name = os.path.join(
            folder,
            f"encrypted_{original_name}"
        )

        write_file(new_file_name, encrypted_content)

        print(f"File encrypted and saved as {new_file_name}")

    elif choice == '2':
        content = read_file(file_name)
        decrypted_content = decrypt_text(content, shift)

        new_file_name = os.path.join(
            folder,
            f"decrypted_{original_name}"
        )

        write_file(new_file_name, decrypted_content)

        print(f"File decrypted and saved as {new_file_name}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()