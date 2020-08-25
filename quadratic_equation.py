from math import sqrt
import tkinter as tk
from tkinter import messagebox as mb


root = tk.Tk()
root.title("Quadratic Equation Solver")


def title_hover(event):
	label_a = event.widget
	label_a.config(bg="#f3fcb1", font=("Bookman Old Style", 21))


def title_leave(event):
	label_a = event.widget
	label_a.config(bg="#77cf90", font=("Bookman Old Style", 20))


def direction_hover(event):
	label_a = event.widget
	label_a.config(bg="#f3fcb1", font=("Bookman Old Style", 14))


def direction_leave(event):
	label_a = event.widget
	label_a.config(bg="#77cf90", font=("Bookman Old Style", 12))


def label_a_hover(event):
	label_a = event.widget
	label_a.config(text="Enter Value of a", font=("calibri", 9), bg="#f3fcb1")


def label_a_leave(event):
	label_a = event.widget
	label_a.config(text=" a ", font=("Bookman Old Style", 13), bg="#e1ffe1")


def label_b_hover(event):
	label_a = event.widget
	label_a.config(text="Enter Value of b", font=("calibri", 9), bg="#f3fcb1")


def label_b_leave(event):
	label_a = event.widget
	label_a.config(text=" b ", font=("Bookman Old Style", 13), bg="#e1ffe1")


def label_c_hover(event):
	label_a = event.widget
	label_a.config(text="Enter Value of c", font=("calibri", 9), bg="#f3fcb1")


def label_c_leave(event):
	label_a = event.widget
	label_a.config(text=" c ", font=("Bookman Old Style", 13), bg="#e1ffe1")


def entry_hover(event):
	label_a = event.widget
	label_a.config(bg="#f3e38d")


def entry_leave(event):
	label_a = event.widget
	label_a.config(bg="#fff8ce")


def button_hover(event):
	button = event.widget
	button.config(bg="#e3f55f")


def button_leave(event):
	button = event.widget
	button.config(bg="#f3ff96")


def lower_hover(event):
	button = event.widget
	button.config(bg="#f3fcb1", font=("arial black", 10))


def lower_leave(event):
	button = event.widget
	button.config(bg="#e1ffe1", font=("arial", 9))


def ans_hover(event):
	button = event.widget
	button.config(font=("Arial", 14), bg="#f3fcb1")


def ans_leave(event):
	button = event.widget
	button.config(font=("Arial", 13), bg="#e1ffe1")


def final_hover(event):
	button = event.widget
	button.config(font=("Arial", 14), bg="#efff74")


def final_leave(event):
	button = event.widget
	button.config(font=("Arial", 13), bg="#f3ff96")


def x_value(a, b, c):
	try:
		x1 = (-b + sqrt(pow(b, 2) - (4*a*c)))/(2*a)
		x2 = (-b - sqrt(pow(b, 2) - (4*a*c)))/(2*a)
	except ValueError:
		from cmath import sqrt as root
		x_1 = (-b + root(pow(b, 2) - (4*a*c)))/(2*a)
		x_2 = (-b - root(pow(b, 2) - (4*a*c)))/(2*a)
		return x_1, x_2
	else:
		return round(x1, 2), round(x2, 2)


def solve():
	try:
		a = entry_a.get()
		b = entry_b.get()
		c = entry_c.get()
		if len(a) == 0 or len(b) == 0 or len(c) == 0:
			mb.showerror(title="Error", message="Complete the Entry Fields")
		else:
			answer = x_value(float(a), float(b), float(c))
			statement = tk.Label(pane, text="The Values of x are:", font=("Arial", 13), bg="#e1ffe1")
			statement.bind("<Enter>", ans_hover)
			statement.bind("<Leave>", ans_leave)
			statement.place(relx=0.34, rely=0.56)
			ans = tk.Label(pane, text=f"{answer}", font=("Arial", 13), bg="#f3ff96")
			ans.bind("<Enter>", final_hover)
			ans.bind("<Leave>", final_leave)
			ans.place(relx=0.02, rely=0.67, relwidth=0.95)
	except ValueError:
		mb.showerror(title="Error", message="Enter Valid Input")


pane = tk.Canvas(root, height="300", width="450", bg="#77cf90")
pane.pack()

title = tk.Label(pane, text="Quadratic Solver", font=("Bookman Old Style", 20), bg="#77cf90")
title.bind("<Enter>", title_hover)
title.bind("<Leave>", title_leave)
title.place(relx=0.23, rely=0.03)

direction = tk.Label(pane, text="Direction: From your Quadratic Equation,\nEnter the value of the following", font=("Bookman Old Style", 12), bg="#77cf90")
direction.bind("<Enter>", direction_hover)
direction.bind("<Leave>", direction_leave)
direction.place(relx=0.06, rely=0.15)

label_a = tk.Label(pane, text=" a ", font=("Bookman Old Style", 13), bg="#e1ffe1")
label_a.bind("<Enter>", label_a_hover)
label_a.bind("<Leave>", label_a_leave)
label_a.place(relx=0.02, rely=0.33)

entry_a = tk.Entry(pane, font=("Bookman Old Style", 13), bg="#fff8ce")
entry_a.bind("<Enter>", entry_hover)
entry_a.bind("<Leave>", entry_leave)
entry_a.place(relx=0.02, rely=0.43, relwidth=0.15)

label_b = tk.Label(pane, text=" b ", font=("Bookman Old Style", 13), bg="#e1ffe1")
label_b.bind("<Enter>", label_b_hover)
label_b.bind("<Leave>", label_b_leave)
label_b.place(relx=0.25, rely=0.33)

entry_b = tk.Entry(pane, font=("Bookman Old Style", 13), bg="#fff8ce")
entry_b.bind("<Enter>", entry_hover)
entry_b.bind("<Leave>", entry_leave)
entry_b.place(relx=0.25, rely=0.43, relwidth=0.15)

label_c = tk.Label(pane, text=" c ", font=("Bookman Old Style", 13), bg="#e1ffe1")
label_c.bind("<Enter>", label_c_hover)
label_c.bind("<Leave>", label_c_leave)
label_c.place(relx=0.48, rely=0.33)

entry_c = tk.Entry(pane, font=("Bookman Old Style", 13), bg="#fff8ce")
entry_c.bind("<Enter>", entry_hover)
entry_c.bind("<Leave>", entry_leave)
entry_c.place(relx=0.48, rely=0.43, relwidth=0.15)

button = tk.Button(pane, text="Solve for x", font=("Arial Black", 15), bg="#f3ff96", activebackground="#b1ba72", command=solve)
button.bind("<Enter>", button_hover)
button.bind("<Leave>", button_leave)
button.place(relx=0.7, rely=0.34, relheight=0.18, relwidth=0.28)

creator = tk.Label(pane, text="Created by: Menard D. Maranan", font=("Arial", 9))
creator.bind("<Enter>", lower_hover)
creator.bind("<Leave>", lower_leave)
creator.place(relx=0.02, rely=0.82)

youtube = tk.Label(pane, text="Search me on YouTube: Menard Maranan Channel", font=("Arial", 9))
youtube.bind("<Enter>", lower_hover)
youtube.bind("<Leave>", lower_leave)
youtube.place(relx=0.02, rely=0.9)

root.mainloop()

