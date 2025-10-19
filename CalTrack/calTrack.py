import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

def graphic():
    file = fileEntry.get()
    if ".csv" in file:
        try:
            df = pd.read_csv(file)
        except:
            label.config(text="File not found")
            return
    elif ".xlsx" in file:
        try:
            df = pd.read_excel(file)
        except:
            label.config(text="File not found")
            return
    else: 
        label.config(text="File format not valid")
        return

    try:
        df["date"] = pd.to_datetime(df["date"]).dt.date
    except:
        label.config(text=f"No date in {file}")
        return
    dailyCal = df.groupby("date")['calories'].sum()
    x = dailyCal.index
    y = dailyCal.values

    colors = ["green" if c > 2000 else "red" for c in y]

    plt.bar(x, y, color=colors)
    plt.title("Calories by Date")
    plt.xlabel("Dates")
    plt.ylabel("Calories")
    plt.show()

screen = tk.Tk()
screen.title("Calories Tracker")
screen.geometry("600x400")

fileEntry = tk.Entry(screen, width=30)
fileEntry.pack()

graphBttn = tk.Button(screen, text="Draw graph", command=graphic)
graphBttn.pack()

label = tk.Label(screen, text="Enter a file")
label.pack()

screen.mainloop()