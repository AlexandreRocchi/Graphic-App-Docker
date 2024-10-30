import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("200x200")
root.title("Test")


def confirm_action():
    messagebox.showinfo("Confirmation", "Test is done!")


root.configure(bg="black")


button = ctk.CTkButton(
    root,
    text="Confirmer",
    text_color="black",
    fg_color="white",
    command=confirm_action
)
button.pack(pady=50)

root.mainloop()
