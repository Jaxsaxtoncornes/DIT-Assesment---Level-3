from tkinter import *

class Items: #Has all the categorys for the products that will be added
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

    def clear_screen(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_screen()
            
        Label(self.parent, text="Inventory Tracker", bg="green", font=("Roboto", 20, "bold")).pack(pady=10)

        Button(self.parent, text="Add Item", command=self.add_item).pack()
        #Button(self.parent, text="View Items", command=self.view_items).pack()
        #Button(self.parent, text="Search", command=self.search_screen).pack()

    def add_item(self):
        self.clear_screen()

        Label(self.parent, text="Add Item").pack()

        name_entry = Entry(self.parent)
        name_entry.pack()

        price_entry = Entry(self.parent)
        price_entry.pack()

        category_entry = Entry(self.parent)
        category_entry.pack()
        
        stock_entry = Entry(self.parent)
        stock_entry.pack()

        def save_item(): #save function for the products
            name = name_entry.get()
            price = price_entry.get()
            category = category_entry.get()
            stock = stock_entry.get()

            if name == "" or price == "" or category == "" or stock == "": #Checks if the user didnt input in a category and will make them enter the data again
                print("Please fill out all fields")
                return

            price = float(price) #Converts text into numnbers
            stock = int(stock)

            new_item = Items(name, price, category, stock) #creates the item
            self.products_list.append(new_item)

            print("Item Added")

        Button(self.parent, text="Save Item", command=save_item).pack()

        Button(self.parent, text="Back", command=self.main_menu).pack()

    def view_items(self):
        self.clear_screen()

        Label(self.parent, text="All Items").pack()

        for item in self.items_list:
            text = item.name + " | $" + str(item.price) + " | " + item.category + " | Stock: " + str(item.stock)
            Label(self.parent, text=text).pack()
        
        Button(self.parent, text="Back", command=self.main_menu).pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Tracker")
    app = Inventory(root)
    root.configure(bg='green')
    root.mainloop()