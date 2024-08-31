import tkinter as tk
from tkinter import messagebox
import csv
import os

# Constants
USER_DB_FILE = "user_data.csv"

# Ensure user data file exists
def create_user_db_file():
    if not os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])

# Function to check if a user exists
def user_exists(username):
    with open(USER_DB_FILE, mode='r') as file:
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
        with open(USER_DB_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        messagebox.showinfo("Success", f"User {username} registered successfully!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

# Function to log in
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    with open(USER_DB_FILE, mode='r') as file:
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
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    btn_login.grid(row=3, column=0, padx=10, pady=10)
    btn_register.grid(row=3, column=1, padx=10, pady=10)
    btn_logout.grid_forget()

# Show logout button
def show_logout(username):
    btn_login.grid_forget()
    btn_register.grid_forget()
    btn_logout.config(text=f"Logout ({username})")
    btn_logout.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Tkinter GUI setup
root = tk.Tk()
root.title("Login System")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Main frame
frame_main = tk.Frame(root, bg="#ffffff", padx=40, pady=40)
frame_main.pack(pady=30)

# Header label
label_header = tk.Label(frame_main, text="Login System", font=("Arial", 24), bg="#ffffff")
label_header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Username and Password labels and entries
label_username = tk.Label(frame_main, text="Username:", font=("Arial", 14), bg="#ffffff")
label_username.grid(row=1, column=0, padx=10, pady=5)

entry_username = tk.Entry(frame_main, font=("Arial", 14), width=25)
entry_username.grid(row=1, column=1, padx=10, pady=5)

label_password = tk.Label(frame_main, text="Password:", font=("Arial", 14), bg="#ffffff")
label_password.grid(row=2, column=0, padx=10, pady=5)

entry_password = tk.Entry(frame_main, show="*", font=("Arial", 14), width=25)
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Login, Register, and Logout buttons
btn_login = tk.Button(frame_main, text="Login", command=login, font=("Arial", 12), bg="#4CAF50", fg="white", width=12)
btn_register = tk.Button(frame_main, text="Register", command=register, font=("Arial", 12), bg="#2196F3", fg="white", width=12)
btn_logout = tk.Button(frame_main, text="Logout", command=lambda: logout(entry_username.get()), font=("Arial", 12), bg="#f44336", fg="white", width=12)

create_user_db_file()
show_login_register()

# Run the application
root.mainloop()
