 import tkinter as tk

def create_main_window():
    root = tk.Tk()
    root.title("Crypto Tracker")
    tk.Label(root, text="Welcome to Crypto Tracker!").pack()
    root.mainloop()

if __name__ == "__main__":
    create_main_window()

