from tkinter import *

class Items:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

class Inventory:
    def __init__(self, parent):

        self.label1 = Label(parent, text="Inventory Tracker", fg="Black", bg='green', font=("Roboto", 20, "bold"))
        self.label1.pack(pady=10)

        button1 = Button(parent, text="Update/Remove Products", relief="flat", borderwidth=0, highlightthickness=0, command=self.press1)
        button1.config(bg="gray")
        button1.pack()  

        button2 = Button(parent, text="Search", relief="flat", borderwidth=0, highlightthickness=0, command=self.press2)
        button2.config(bg="gray")
        button2.pack()

    def press1(self):
            print("Update/Remove Products")
    
    def press2(self):
            print("Search")


if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Tracker")
    app = Inventory(root)
    root.configure(bg='green')
    root.mainloop()