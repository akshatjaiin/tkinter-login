# 🛡️ Simple Tkinter Login System

This project is a **Simple Login System** built using Python's Tkinter library. It provides a basic GUI for user registration, login, and logout functionalities, with user data being stored in a CSV file. This is a great starting point for beginners looking to learn about GUI development in Python and basic user authentication.

## 🎯 Features

- **User Registration**: Allows new users to register by entering a username and password.
- **User Login**: Existing users can log in by providing their credentials.
- **Logout Functionality**: Logged-in users can log out easily.
- **Data Persistence**: User data is stored in a CSV file (`user_data.csv`), ensuring persistence across sessions.
- **Responsive GUI**: The interface is designed with Tkinter, offering a simple yet responsive design.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/tkinter-login.git
   cd tkinter-login-system
Ensure Python is installed:

This project is compatible with Python 3.x. You can check your Python version by running:
bash
Copy code
python --version
Run the application:

Simply execute the login_system.py file:
bash
Copy code
python login_system.py
📁 Project Structure
login_system.py: The main script containing the Tkinter GUI and functionality.
user_data.csv: A CSV file where user credentials are stored.
🧰 How It Works
User Registration: The system checks if a username already exists in the user_data.csv file. If it doesn't, the new username and password are stored.

User Login: The system verifies the username and password against the data in user_data.csv. If a match is found, the user is logged in; otherwise, an error message is shown.

User Logout: When a user logs out, the interface returns to the initial login/register state.

🖼️ Screenshots
Login Screen

Register Screen

🚀 Future Improvements
Password Hashing: Implement password hashing for improved security.
Improved UI: Enhance the user interface with more modern design elements.
User Management: Add functionality for password recovery and user deletion.
🤝 Contribution
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements or features.


