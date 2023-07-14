import random
import string
import csv

PASSWORD_LENGTH = 10

def generate_password():
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(PASSWORD_LENGTH))
        
        if (any(c.islower() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.isdigit() for c in password) and 
            any(c in string.punctuation for c in password)):
            return password

website = input("Enter the name of the website: ")
email = input("Enter the email associated with the website: ")
username = input("Enter the username associated with the website (leave blank if none): ")
username = username if username else "none"
password = generate_password()

print("Password is: ", password)

with open("password.csv", 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([website, email, username, password])

print("Password saved to password.csv")