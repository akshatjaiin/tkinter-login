import tkinter as tk
from tkinter import messagebox
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
def register():
    username = entry_username.get()
    password = entry_password.get()
    
    if user_exists(username):
        messagebox.showerror("Error", "Username already exists.")
    else:
        with open(user_db_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        messagebox.showinfo("Success", f"User {username} registered successfully!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

# Function to log in
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    with open(user_db_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                show_logout(username)
                return
    messagebox.showerror("Error", "Invalid username or password.")

# Function to log out
def logout(username):
    messagebox.showinfo("Goodbye", f"Goodbye, {username}!")
    show_login_register()

# Show login and register buttons
def show_login_register():
    btn_login.pack()
    btn_register.pack()
    btn_logout.pack_forget()
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Show logout button
def show_logout(username):
    btn_login.pack_forget()
    btn_register.pack_forget()
    btn_logout.config(text=f"Logout ({username})")
    btn_logout.pack()

# Tkinter GUI setup
root = tk.Tk()
root.title("Login System")

# Username and Password labels and entries
label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Login, Register, and Logout buttons
btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack()

btn_register = tk.Button(root, text="Register", command=register)
btn_register.pack()

btn_logout = tk.Button(root, text="Logout", command=lambda: logout(entry_username.get()))

show_login_register()

# Run the application
root.mainloop()
