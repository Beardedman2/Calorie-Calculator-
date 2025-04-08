import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def calculate_calories():
    try:
        
        food = food_var.get()
        quantity = float(entry_quantity.get())
        
        #this is the calories of specific items.
        food_calories = {
            "Apple": 95,
            "Banana": 105,
            "Chicken ": 239,
            "Rice": 206,
            "Broccoli": 34,
            "White Bread": 265,
            "Pasta": 131,
            "SkipJackTuna": 132,
            "Chedder Cheese": 402,
            "Potato Chips": 536,
             
        }

        
        total_calories = food_calories[food] * quantity
        
       
        label_result.config(text=f"Total Calories: {total_calories:.2f} cal")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid amount.")


def clear_entries():
    food_var.set("Apple")  
    entry_quantity.delete(0, tk.END)
    label_result.config(text="Total Calories: ")


def exit_app():
    window.quit()


window = tk.Tk()
window.title("Food Calorie Calculator")
window.geometry("350x300")

# the labels that are on Display.
label_food = tk.Label(window, text="Select food item:")
label_food.pack(pady=5)

#This is the Text you see on display when choosing a item.
food_var = tk.StringVar()
food_combobox = ttk.Combobox(window, textvariable=food_var, values=["Apple", "Banana", "Chicken ", "Rice", "Broccoli", "White Bread", "Pasta", "SkipJackTuna", "Chedder Cheese", "Potato Chips"])  
food_combobox.set("Apple")  
food_combobox.pack(pady=5)

#this is the Text label for the amount of servings.
label_quantity = tk.Label(window, text="Enter The Amount (servings):")
label_quantity.pack(pady=5)


entry_quantity = tk.Entry(window)
entry_quantity.pack(pady=5)


label_result = tk.Label(window, text="Total Calories: ")
label_result.pack(pady=10)


button_calculate = tk.Button(window, text="Calculate", command=calculate_calories)
button_calculate.pack(pady=5)

button_clear = tk.Button(window, text="Clear", command=clear_entries)
button_clear.pack(pady=5)

button_exit = tk.Button(window, text="Exit", command=exit_app)
button_exit.pack(pady=5)



window.mainloop()
