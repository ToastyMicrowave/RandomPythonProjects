import json
from tkinter import Entry, Tk, Button, Label, PhotoImage, Canvas, messagebox
from tkinter.constants import END
import random
FONT = ("BaskervilleSerial", 14, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choices(letters, k=nr_letters), random.choices(
        symbols, k=nr_symbols), random.choices(numbers, k=nr_numbers)]

    # Flattening list
    password_list = [
        item for pass_sublist in password_list for item in pass_sublist]

    random.shuffle(password_list)

    password_entry.delete(0, END)
    password_entry.insert(index=0, string=''.join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email_or_user = email_user_entry.get()
    password = password_entry.get()
    data_dict = {
        website: {
            "Email/User": email_or_user,
            "password": password
        }
    }
    for field in [website, email_or_user, password]:
        if len(field) < 1:
            messagebox.showerror(
                title="Oops", message="Please don't leave any fields empty!")
            return
    user_confirm = messagebox.askokcancel(
        title=website,
        message=f"""\
These are the details entered:
Email/Username: {email_or_user}
Password: {password}
Is it ok to save?\
""")

    if user_confirm:
        try:
            with open(r"C:\Python Projects\Password Manager\data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(data_dict)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = data_dict
        finally:
            with open(r"C:\Python Projects\Password Manager\data.json", "w") as data_file:
                json.dump(obj=data, fp=data_file, indent=4)
            website_entry.delete(0, END)
            email_user_entry.delete(0, END)
            password_entry.delete(0, END)

# ------------------------------SEARCH -------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open(r"C:\Python Projects\Password Manager\data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror(
            title="oops", message="Sorry, there are no entries in our database.")
        return
    if website in data:
        email_or_user = (data[website]["Email/User"])
        password = (data[website]["password"])
        messagebox.showinfo(title=website, message=f"""\
The credentials for {website} are:
Email/Username: {email_or_user}
Password: {password}\
""")
    else:
        messagebox.showerror(
            title="oops", message=f"Sorry, there are no credentials for {website} in our database.\
Make sure it is spelled correctly.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file=r"C:\Python Projects\Password Manager\logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="E-mail/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, sticky="W")
website_entry.focus()

email_user_entry = Entry(width=30)
email_user_entry.grid(column=1, row=2, sticky="W")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")

search_button = Button(command=search, text="Search", width=14)
search_button.grid(column=2, row=1)

generate_pass_button = Button(
    command=password_gen,
    text="Generate Password")
generate_pass_button.grid(column=2, row=3, sticky="W")

add_button = Button(command=save, text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")


window.mainloop()
