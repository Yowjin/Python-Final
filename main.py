from customtkinter import *
from user_database import create_table, insert_user, find_user, update_user_password
from menu import open_menu_window
from PIL import Image, ImageTk

def login():
    username = user_entry.get()
    password = UserPassword_entry.get()

    user = find_user(username, password)

    if user:
        print("Login successful!")
        show_message("Login Successful", open_menu=True)
        window.destroy()
    else:
        existing_user = find_user(username, None)
        if existing_user:
            print("Invalid password!")
            show_message("Invalid password!", return_to_login=True)
        else:
            print("User not found!")
            show_message("User not found!", return_to_login=True)

def signup():
    username = user_entry.get()
    password = UserPassword_entry.get()

    existing_user = find_user(username, None)
    if existing_user:
        print("Username already exists!")
        show_message("Username already exists!")
    else:
        insert_user(username, password)
        print("User registered successfully!")
        show_message("User Created Successfully")

def forgot_password():
    def reset_password():
        username = username_entry.get()
        new_password = new_password_entry.get()
        update_user_password(username, new_password)
        show_message("Password updated successfully!", forgot_password_window.destroy(), return_to_login=True)
        

    forgot_password_window = CTk()
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("300x200")
    forgot_password_window.resizable(False, False)

    username_label = CTkLabel(forgot_password_window, text="Enter Username:")
    username_label.pack(pady=5)

    username_entry = CTkEntry(forgot_password_window)
    username_entry.pack(pady=5)

    new_password_label = CTkLabel(forgot_password_window, text="Enter New Password:")
    new_password_label.pack(pady=5)

    new_password_entry = CTkEntry(forgot_password_window, show="*")
    new_password_entry.pack(pady=5)

    submit_btn = CTkButton(forgot_password_window, text="Submit", command=reset_password)
    submit_btn.pack(pady=5)
    
    forgot_password_window.mainloop()

def show_message(message, open_menu=False, return_to_login=False):
    def close_windows():
        message_window.destroy()
        if open_menu:
            window.destroy()
            open_menu_window()
        elif return_to_login:
            user_entry.delete(0, 'end')
            UserPassword_entry.delete(0, 'end')
            user_entry.focus()
        else:
            window.destroy()

    message_window = CTk()
    message_window.title("Message")
    message_window.geometry("300x100")
    message_window.resizable(False, False)

    message_label = CTkLabel(message_window, text=message)
    message_label.pack(pady=20)

    ok_button = CTkButton(master=message_window, text="OK", corner_radius=10, command=close_windows)
    ok_button.pack()

    message_window.mainloop()

window = CTk()
window.title("Login")
window.geometry("700x500")
window.resizable(False, False)

set_appearance_mode("dark")

title = CTkLabel(window, text="Welcome To CRS", fg_color="transparent", text_color="white", font=("Madimi One", 45))
title.place(relx=0.5, rely=0.2, anchor="center")

entry_frame = CTkFrame(window,fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
entry_frame.place(relx=0.5, rely=0.4, anchor="center")

user_entry = CTkEntry(entry_frame, placeholder_text="Username")
user_entry.pack(fill="x", padx=10, pady=5)

UserPassword_entry = CTkEntry(entry_frame, placeholder_text="Password", show="*")
UserPassword_entry.pack(fill="x", padx=10, pady=5)

login_btn = CTkButton(master=window, text="Login", corner_radius=32, fg_color="transparent", hover_color="#4682B4", border_color="#FFCC70", border_width=2, command=login)
login_btn.place(relx=0.5, rely=0.6, anchor="center")

signup_btn = CTkButton(master=window, text="Sign Up", corner_radius=32, fg_color="transparent", border_color="#FFCC70", border_width=2, command=signup)
signup_btn.place(relx=0.5, rely=0.7, anchor="center")

forgot_password_btn = CTkButton(master=window, text="Forgot Password", corner_radius=32, fg_color="transparent", border_color="#FFCC70", border_width=2, command=forgot_password)
forgot_password_btn.place(relx=0.5, rely=0.8, anchor="center")

create_table()

window.mainloop()
