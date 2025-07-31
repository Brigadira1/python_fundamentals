import tkinter as tk

root = tk.Tk()
root.wm_title("Mile to Km Converter")
root.wm_minsize(width=600, height=300)


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.60934
    calc_label.configure(text=km)


frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame, width=10)
entry.grid_configure(padx=10, pady=10)
entry.grid(row=0, column=1)

miles_label = tk.Label(frame, text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tk.Label(frame, text="is equal to")
is_equal_label.configure(padx=20)
is_equal_label.grid(row=1, column=0)

calc_label = tk.Label(frame, text="0")
calc_label.grid(row=1, column=1)


km_label = tk.Label(frame, text="Km")
km_label.grid(row=1, column=2)

calculate_button = tk.Button(frame, text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

root.mainloop()
