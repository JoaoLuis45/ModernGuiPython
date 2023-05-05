import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x300")
root.title('Login')


def login():
    print("Teste")

frame = ctk.CTkFrame(master=root)
frame.pack(fill="both",expand=True)

label = ctk.CTkLabel(master=frame,text='Login System',font=("Roboto",24))
label.pack(pady=12,padx=10)

entryUsername = ctk.CTkEntry(master=frame,placeholder_text="Username")
entryUsername.pack(pady=12,padx=10)

entryPassword = ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
entryPassword.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember me')
checkbox.pack(pady=12,padx=10)

root.mainloop()