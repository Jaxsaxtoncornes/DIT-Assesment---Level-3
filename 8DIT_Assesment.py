from tkinter import *

class Items:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

class Inventory:
    def __init__(self, parent):
        self.parent = parent
        self.products_list = []

        self.main_menu()

    def main_menu(self):
            
        Label(self.parent, text="Inventory Tracker", bg="green", font=("Roboto", 20, "bold")).pack(pady=10)

        Button(self.parent, text="Add Item", command=self.add_item).pack()
        Button(self.parent, text="View Items", command=self.view_items).pack()
        Button(self.parent, text="Search", command=self.search_screen).pack()

    def add_item(self):

        Label(self.parent, text="Add Item").pack(

        name_entry = Entry(self.parent)
        name_entry.pack()

        price_entry = Entry(self.parent)
        price_entry.pack()

        catergory_entry = Entry(self.parent)
        category_entry.pack()
        
        stock_entry = Entry(self.parent)
        stock_entry.pack()






if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Tracker")
    app = Inventory(root)
    root.configure(bg='green')
    root.mainloop()