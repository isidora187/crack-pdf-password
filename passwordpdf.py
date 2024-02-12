import pikepdf
import time
from colorama import Fore

def crack_password(pdf_file, password_file):
    try:
        with open(password_file, 'r') as passwords:
            start_time = time.time()
            for i, password in enumerate(passwords, start=1):
                password = password.strip()
                print(f"\r{i} Password is being tested: {password}", end="")
                try:
                    pikepdf.open(pdf_file, password=password)
                    end_time = time.time()
                    print("\n")
                    print(f"Password found in {end_time - start_time:.2f} seconds")
                    print(f"Password is: {password}")
                    break
                except pikepdf.PasswordError:
                    pass
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    pdf_file = "200-most-common-passwords-en-protected.pdf"
    password_file = "YourPasswordFileName.txt"
    crack_password(pdf_file, password_file)
