from cryptography.fernet import Fernet
import hashlib
import os

def generate_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)
    print ("Key generated and saved. ")
    
def load_key():
    if not os.path.exists("key.key"):
        print ("Encryption key not found. Please generate key first.")
        exit()
    with open ("key.key", "rb") as key_file:
        return key_file.read()

#Encrypt a password
def encrypt (password,key):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

#Decrypt a Password
def decrypt(encrypted_password,key):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

#Master Password creation to ensure auhtorized users only 
Master_Password_Hash= hashlib.sha256("Mypassword123$".encode()).hexdigest()

def authenticate():
    password = input("Enter the master password: ")
    if hashlib.sha256(password.encode()).hexdigest() != Master_Password_Hash:
        print ("Incorrect Password. Exiting")
        exit()
    print ("Access Granted. \n") 
    
#Save the password to a file
    
def save_password(account,password):
    key = load_key()
    encrypted_password =encrypt(password,key)
    with open ("passwords.txt","a") as file:
        file.write(f"{account}:{encrypted_password}\n")
    print ("Password saved.")

# Retrieve and decrypt the passwords from file   
def retrieve_passwords():
    key = load_key()
    try:
        with open ("passwords.txt","r") as file:
            for line in file:
                line =line.strip()
                if not line or ":" not in line:
              
                    continue
                try:
                    account, encrypted_password = line.split(":",1)
                    decrypted_password = decrypt(encrypted_password,key)
                    print(f"Account: {account}, Password: {decrypted_password}")
                except Exception:
                    continue
    except FileNotFoundError:
        print("No passwords saved yet. Please save a password first.")
    except Exception as e:
        print(f"An error occurred {e}")
        
# Main menu for user to interact with 
def main():
    authenticate()
    while True:
        print ("\nPassword Manager")
        print("1. Save a Password ")
        print("2. Retrieve Passwords ")
        print("3. Exit")
        choice =input("Choose an option:")
          
        if choice == "1":
            account = input ("Enter the account name: ")
            password = input("Enter the password: ")
            save_password(account,password)
        elif choice == "2":
            retrieve_passwords()
        elif choice == "3":
            print ("Exiting")
        break
if  __name__ == "__main__":
    main()

        
