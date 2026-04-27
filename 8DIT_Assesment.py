from tkinter import *

class Items:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

class Inventory:
    def __init__(self, parent):


        self.label1 = Label(parent, text="Buy/Sell Products", font=("Arial", 14))
        self.label1.pack(pady=10)

        self.label2 = Label(parent, text="Update/Remove Products", font=("Arial", 14))
        self.label2.pack(pady=10)

        self.label3 = Label(parent, text="Search", font=("Arial", 14))
        self.label3.pack(pady=10)



if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Tracker")
    app = Inventory(root)
    root.mainloop()