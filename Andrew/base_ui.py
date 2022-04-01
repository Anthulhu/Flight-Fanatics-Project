import random
import tkinter as tk
import requests

def number():
    flight = enter.get()
    enter.delete(0, tk.END)
    lbl_result["text"] = "Delay chance: " + str(random.randint(1, 100)) + "%"

#creates the application Window
window = tk.Tk()
window.title("Delay Prediction")
greeting = tk.Label(
    text="Enter your flight number",
)
greeting.pack()

#allows user to input their information
enter = tk.Entry()
enter.pack()

#submit button for the information
solve = tk.Button(
    text="Click",
    width=10,
    command = number
)
#output result
solve.pack()
lbl_result = tk.Label()
lbl_result.pack()



window.mainloop()
