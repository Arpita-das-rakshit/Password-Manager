from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if not has_upper:
        return "Password must contain at least one uppercase letter"
    if not has_lower:
        return "Password must contain at least one lowercase letter"
    if not has_digit:
        return "Password must contain at least one digit"
    if not has_special:
        return "Password must contain at least one special character"

    return True

# password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    # password=""
    # for char in password_list:
    # password+=char
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----
# -------- SAVE FUNCTION --------
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you have not left any field empty")
        return

    # ✅ VALIDATE PASSWORD HERE
    validation_result = validate_password(password)

    if validation_result != True:
        messagebox.showerror(title="Invalid Password", message=validation_result)
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n{website} | {email} | {password}"
    )
    # ✅ CHECK STRANGTH OF PASSWORD HERE
    strangth= check_strength(password)
    if strangth=="Weak":
        messagebox.showerror(title="Weak Password", message=strangth)
    elif strangth=="Medium":
        messagebox.showerror(title="Weak Password", message=strangth)

#    --------------------
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}|{email}|{password}\n")  # ✅ newline added
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# --------UI SETUP----
window = Tk()
window.title("password manager")
window.config(padx=20, pady=20)
# canvas
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="passwordmanegerlogo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)
# lables
website_lable = Label(text="Website")
website_lable.grid(row=1, column=0)
email_lable = Label(text="email/username")
email_lable.grid(row=2, column=0)
password_lable = Label(text="password")
password_lable.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "arpitadas1234@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()