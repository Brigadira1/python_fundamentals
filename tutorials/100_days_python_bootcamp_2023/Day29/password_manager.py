import json
import random
import string
import tkinter
from pathlib import Path
from tkinter import Button, Canvas, Entry, Frame, Label, PhotoImage, Tk, messagebox

import pyperclip

current_path: Path = Path(__file__).resolve().parent
path_to_pgn = current_path / "logo.png"
# path_to_psd = current_path / "passwords.txt"
path_to_psd = current_path / "data.json"

root = Tk()
root.wm_title("Iavor Password Manager")
root.configure(padx=20, pady=20)


frame = Frame(root)
frame.grid(row=0, column=0)

canvas = Canvas(frame, width=200, height=200)


# def add() -> None:
#
#     website: str = website_entry.get()
#     email: str = email_entry.get()
#     password: str = password_entry.get()
#     delimeter: str = " | "
#
#     create_psd_file(path_to_psd)
#
#     if not validate_user_input(website, password):
#         messagebox.showwarning(
#             title="Validation failed",
#             message="Email and/or password entries cannot be empty",
#         )
#         return
#
#     is_ok = messagebox.askokcancel(
#         title=website,
#         message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?",
#     )
#
#     if is_ok:
#
#         new_row: str = website + delimeter + email + delimeter + password + "\n"
#
#         if not check_entry_exists(website, path_to_psd):
#             persist_new_row(new_row, path_to_psd)
#         else:
#             update_entry(website, new_row, path_to_psd)
#
#         website_entry.delete(0, tkinter.END)
#         password_entry.delete(0, tkinter.END)


def add():

    website: str = website_entry.get()
    email: str = email_entry.get()
    password: str = password_entry.get()

    if not validate_user_input(website, password):
        messagebox.showwarning(
            title="Validation failed",
            message="Email and/or password entries cannot be empty",
        )
        return

    new_data = {website: {email: password}}

    try:

        with path_to_psd.open("r") as data_file:
            current_data = json.load(data_file)

    except FileNotFoundError:

        with path_to_psd.open("w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        current_data.update(new_data)

        with path_to_psd.open("w") as data_file:
            json.dump(current_data, data_file, indent=4)

    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)


def create_psd_file(path_to_psd: Path) -> None:
    if not path_to_psd.exists():
        path_to_psd.touch()


def validate_user_input(website: str, password: str) -> bool:
    if website and password:
        return True
    else:
        return False


def persist_new_row(new_row: str, file: Path) -> None:

    with file.open(mode="a", encoding="utf-8") as f:
        f.write(new_row)


def check_entry_exists(website: str, path_to_psd: Path) -> bool:
    with path_to_psd.open(mode="r", encoding="utf-8") as pass_file:
        for line in pass_file:
            if line.startswith(website):
                return True

    return False


def update_entry(website: str, updated_row: str, path_to_psd: Path) -> None:
    updated_file_contents: list[str] = []
    with path_to_psd.open(mode="r", encoding="utf-8") as pass_file:
        for line in pass_file:
            if line.startswith(website):
                updated_file_contents.append(updated_row)
            else:
                updated_file_contents.append(line)
    create_backup(path_to_psd)

    with open(path_to_psd, "w") as temp:
        temp.writelines(updated_file_contents)


def create_backup(path_to_psd: Path) -> None:
    backup_file = path_to_psd.parent / (path_to_psd.name + ".bak")
    backup_file.write_bytes(path_to_psd.read_bytes())


def generate_passwd():

    rand_password = ""

    for _ in range(5):

        rand_letter = random.choice(list(string.ascii_letters))
        rand_number = random.choice(list(string.digits))
        rand_symbol = random.choice(list(string.punctuation))

        rand_password += rand_letter + rand_number + rand_symbol

    rand_password_list = list(rand_password)
    random.shuffle(rand_password_list)
    rand_password = "".join(rand_password_list)
    password_entry.insert(0, rand_password)
    pyperclip.copy(rand_password)


def search():
    pass


my_pass_img = PhotoImage(file=path_to_pgn)
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)

website = Label(frame, text="Website:")
website.grid(row=1, column=0)

email_username = Label(frame, text="Email/Username:")
email_username.grid(row=2, column=0)

password = Label(frame, text="Password:")
password.grid(row=3, column=0)

website_entry = Entry(frame, width=25)
website_entry.focus_force()
website_entry.grid(row=1, column=1, sticky="w")

search_button = Button(frame, text="Search", width=15, command=search)
search_button.grid(row=1, column=1, sticky="e")

email_entry = Entry(frame, width=35)
email_entry.insert(0, "iavor.stoimenov@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(frame, width=35)
password_entry.grid(row=3, column=1, sticky="w")

generate_password = Button(
    frame, text="Generate Password", width=15, command=generate_passwd
)
generate_password.grid(row=3, column=1, sticky="e")


add_button = Button(frame, text="Add", width=29, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


root.mainloop()
