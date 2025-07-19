from os import pathconf
from pathlib import Path
from tkinter import Button, Canvas, Entry, Frame, Label, PhotoImage, Tk

current_path: Path = Path(__file__).resolve().parent
path_to_pgn = current_path / "logo.png"
path_to_psd = current_path / "passwords.txt"

pass_cache: dict[str, list[str]] = {}

root = Tk()
root.wm_title("Iavor Password Manager")
root.configure(padx=20, pady=20)


frame = Frame(root)
frame.grid(row=0, column=0)

canvas = Canvas(frame, width=200, height=200)


def add() -> None:

    website: str = website_entry.get()
    email: str = email_entry.get()
    password: str = password_entry.get()
    delimeter: str = " | "

    create_psd_file(path_to_psd)

    if not validate_user_input(website, email, password):
        print("Website, email and/or password entries cannot be empty")
        return

    new_row: str = website + delimeter + email + delimeter + password + "\n"

    if not check_entry_exists(website, path_to_psd):
        persist_new_row(new_row, path_to_psd)
    else:
        update_entry(website, email, password, new_row, path_to_psd)


def create_psd_file(path_to_psd: Path) -> None:
    if not path_to_psd.exists():
        path_to_psd.touch()


def validate_user_input(website: str, email: str, password: str) -> bool:
    if website and email and password:
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


def update_entry(
    website: str, email: str, password: str, updated_row: str, path_to_psd: Path
) -> None:
    updated_file_contents: list[str] = []
    with path_to_psd.open(mode="r", encoding="utf-8") as pass_file:
        for line in pass_file:
            if line.startswith(website):
                updated_file_contents.append(updated_row)
            else:
                updated_file_contents.append(line)
    temp_file = current_path / "temp_password_file.txt"
    with open(temp_file, "w") as temp:
        temp.writelines(updated_file_contents)


my_pass_img = PhotoImage(file=path_to_pgn)
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)

website = Label(frame, text="Website:")
website.grid(row=1, column=0)

email_username = Label(frame, text="Email/Username:")
email_username.grid(row=2, column=0)

password = Label(frame, text="Password:")
password.grid(row=3, column=0)

website_entry = Entry(frame, width=35)
website_entry.focus_force()
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_entry = Entry(frame, width=35)
email_entry.insert(0, "iavor.stoimenov@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(frame, width=35)
password_entry.grid(row=3, column=1, sticky="w")

generate_password = Button(frame, text="Generate Password", width=15)
generate_password.grid(row=3, column=1, sticky="e")


add_button = Button(frame, text="Add", width=29, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


root.mainloop()
