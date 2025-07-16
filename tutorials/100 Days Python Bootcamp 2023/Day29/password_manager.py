from pathlib import Path
from tkinter import Button, Canvas, Entry, Frame, Label, PhotoImage, Tk

root = Tk()
root.wm_title("Iavor Password Manager")
root.configure(padx=20, pady=20)

frame = Frame(root)
frame.grid(row=0, column=0)

canvas = Canvas(frame, width=200, height=200)

path_to_pgn = Path(__file__).resolve().parent / "logo.png"
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
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_entry = Entry(frame, width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(frame, width=35)
password_entry.grid(row=3, column=1, sticky="w")

generate_password = Button(frame, text="Generate Password", width=15)
generate_password.grid(row=3, column=1, sticky="e")

add_button = Button(frame, text="Add", width=29)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


root.mainloop()
