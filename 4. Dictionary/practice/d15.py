'User Login Validation'

users = {
    "dhvanit": "12345",
    "admin": "admin@123",
    "user1": "pass123"
}

username = input("Enter a username: ")
password = input("Enter a password: ")

if username in users and users[username] == password:
    print("Login Successfully")
else:
    print("Invalid Username and password")