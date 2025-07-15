from pathlib import Path
from tkinter import Button, Canvas, Label, PhotoImage, Tk

root = Tk()
root.wm_title("Iavor Passord Manage")
root.configure(width=800, height=800, pady=20)

canvas = Canvas(root, width=400, height=400)
path: Path = Path(__file__).resolve().parent
path_to_pgn = path / "logo.png"
print(path_to_pgn)
my_pass_img = PhotoImage(file=path_to_pgn, height=200, width=200)
canvas.create_image(200, 200, image=my_pass_img)
canvas.pack()


root.mainloop()
