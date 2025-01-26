# Python Password Manager 
A simple and secure password manager built with Python using AES-based encryption.
# Features
* Encrypt and securely store passwords using AES-based encryption.
* Retrieve and decrypt passwords with user authentication.
* Master Password authentication using SHA 256- hashing. 
# Installation
1. Clone the repository:
 git clone https://github.com/CARLG2022/Python-Password-Manager.git
2. Navigate to the project library:
cd Python-Password-Manager
3. Install the required library:
   pip install cryptography
4. Run the program:
   python password_manager.py
5. Generate the encryption key if it's the first time running the program:

    from password_manager import generate_key
    generate_key()
# License
This project is licensed under the MIT License – see the LICENSE file for details.
