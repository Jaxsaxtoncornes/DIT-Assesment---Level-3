from tkinter import *

class Items:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

class Inventory:
    def __init__(self, parent):

        self.label1 = Label(parent, text="Inventory Tracker", fg="Black", bg='olive', font=("Roboto", 20, "bold"))
        self.label1.pack(pady=10)

        button1 = Button(parent, text="Buy/Sell Products", command=self.press1)
        button1.config(bg="gray")
        button1.pack()

        button2 = Button(parent, text="Update/Remove Products", command=self.press2)
        button2.config(bg="gray")
        button2.pack()  

        button3 = Button(parent, text="Search", command=self.press3)
        button3.config(bg="gray")
        button3.pack()

    def press1(self):
         print("Buy/Sell Products")

    
    def press2(self):
            print("Update/Remove Products")
    
    def press3(self):
            print("Search")


if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Tracker")
    app = Inventory(root)
    root.configure(bg='olive')
    root.mainloop()