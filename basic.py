import csv
import os

# File to store user data
user_db_file = "user_data.csv"

# Ensure user data file exists
if not os.path.exists(user_db_file):
    with open(user_db_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])

# Function to check if a user exists
def user_exists(username):
    with open(user_db_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

# Function to register a new user
def register(username, password):
    if user_exists(username):
        print("Username already exists.")
        return False
    else:
        with open(user_db_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print(f"User {username} registered successfully!")
        return True

# Function to log in
def login(username, password):
    with open(user_db_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print(f"Welcome, {username}!")
                return True
    print("Invalid username or password.")
    return False

# Function to log out
def logout(username):
    print(f"Goodbye, {username}!")

def main():
    logged_in = False
    username = None

    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            register(new_username, new_password)
        
        elif choice == '2':
            if not logged_in:
                username = input("Enter username: ")
                password = input("Enter password: ")
                logged_in = login(username, password)
            else:
                print(f"Already logged in as {username}.")
        
        elif choice == '3':
            if logged_in:
                logout(username)
                logged_in = False
                username = None
            else:
                print("No user is currently logged in.")
        
        elif choice == '4':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
