import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        skib1 = float(e1.get())
        skib2 = float(e2.get())
        operation = opvar.get()
        
        if operation == "Add":
            result = skib1 + skib2      
        elif operation == "Subtract":
            result = skib1 - skib2
        elif operation == "Multiply":
            result = skib1 * skib2
        elif operation == "Divide":
            if skib2 != 0:
                result = skib1 / skib2
            else:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
        else:
            result = "Invalid Operation"
        
        resultl.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")


e1 = tk.Entry(root, width=10)
e1.grid(row=0, column=1, padx=10, pady=10)

e2 = tk.Entry(root, width=10)
e2.grid(row=1, column=1, padx=10, pady=10)

label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0)

opvar = tk.StringVar(value="Add")
operations_menu = tk.OptionMenu(root, opvar, "Add", "Subtract", "Multiply", "Divide")
operations_menu.grid(row=2, column=1, padx=10, pady=10)

operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=2, column=0)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

resultl = tk.Label(root, text="Result:")
resultl.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

