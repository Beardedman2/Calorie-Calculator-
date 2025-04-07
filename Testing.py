import customtkinter

def button_callback():
    print("Your Button")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Button 1", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)
app.grid_columnconfigure(0, weight=1)


button = customtkinter.CTkButton(app, text="Press", command=button_callback)
button.grid(row=1, column=1,padx=10, pady=10)
app.mainloop()