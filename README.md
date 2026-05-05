# Password-Manager
This is a simple desktop Password Manager application built using Python and Tkinter. It helps users generate strong passwords, validate them, and securely store login credentials (website, email, and password) in a local file.
Features

# Generate strong random passwords
-> Copy generated password automatically to clipboard
-> Validate password with security rules
-> Check password strength (Weak / Medium / Strong)
-> Store credentials locally in a text file
-> Simple and user-friendly GUI using Tkinter

#Technologies Used
-> Python
-> Tkinter (for GUI)
-> Random module (password generation)
-> Pyperclip (clipboard copy)

#Project Structure
-> manager.py → Main application file (GUI + logic)
-> data.txt → Stores saved credentials
-> passwordmanegerlogo.png → Logo used in UI

# How It Works
-> Enter Website name
-> Enter Email/Username
-> Click "Generate Password" (optional)
-> Click "Add"
-> Password is validated and checked for strength
-> Data is saved into data.txt

#Password Rules
-> Minimum 8 characters
-> At least one uppercase letter
-> At least one lowercase letter
-> At least one digit
-> At least one special character

#Installation & Setup
-> Clone the repository
-> Install required library:
  -> pip install pyperclip
-> Run the application:
  -> manager.py
