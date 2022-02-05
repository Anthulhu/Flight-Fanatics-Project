import random
import tkinter as tk

def number():
    flight = enter.get()
    enter.delete(0, tk.END)
    lbl_result["text"] = "Delay chance: " + str(random.randint(1, 100)) + "%"

window = tk.Tk()
window.title("Delay Prediction")
greeting = tk.Label(
    text="Enter your flight number",
)
greeting.pack()

enter = tk.Entry()
enter.pack()

solve = tk.Button(
    text="Click",
    width=10,
    command = number
)
solve.pack()
lbl_result = tk.Label()
lbl_result.pack()


window.mainloop()
