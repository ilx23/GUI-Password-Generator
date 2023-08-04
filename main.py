from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import json

# ---------------------------- SEARCH WEBSITE INFORMATION ------------------------------- #
def find_password():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as data_value:
            data = json.load(data_value)
            try:
                website_data = data[website_name]
                website_email = website_data['email']
                website_password = website_data["password"]
                messagebox.showinfo(title=website_name, message=f"Email: {website_email} \n Password: {website_password}")
            except KeyError:
                messagebox.showinfo(title="Error", message="No Data File Found")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    password_entry.select_range(0, END)
    password_entry.event_generate("<<Copy>>")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \n Email: {email}"
                                                              f"\n Password: {password} \n is it ok to save? ")
        if is_ok:
            try:
                with open("data.json", "r") as data_value:
                    data = json.load(data_value)
            except FileNotFoundError:
                with open("data.json", "w") as data_value:
                    json.dump(new_data, data_value, indent=4)
            else:

                data.update(new_data)


                with open("data.json", "w") as data_value:
                    json.dump(data, data_value, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website Name: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Your Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Your Password: ")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=27)
website_entry.grid(row=1, column=1, columnspan=1)
email_entry = Entry(width=47)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "iliakeshavarz23@gmail.com")
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

#buttons
generate_btn = Button(text="Generate Password", command=password_generator, width=15)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=24, command=save_data)
add_btn.grid(row=4, column=1, columnspan=1)
search_btn = Button(text='Search', command=find_password, width=15)
search_btn.grid(row=1, column=2)






window.mainloop()