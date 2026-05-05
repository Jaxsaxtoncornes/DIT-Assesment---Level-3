from tkinter import *

class Items: # The blueprint for each item, the item will have a name, price, category, and stock
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock


class Inventory:
    def __init__(self, parent):
        self.parent = parent
        self.products_list = [] # Will store all items

        self.main_menu() # When the code runs this will be the first thing to run, which dispalys the menu


    def clear_screen(self):
        for widget in self.parent.winfo_children(): # returns all widgets that are on the window
            widget.destroy() # Removes the widget from the screen, allow the code to change windows/screen


    def main_menu(self):
        self.clear_screen() # This will clear the old screen that was last used

        Label(self.parent, text="Inventory Tracker", bg="green", font=("Roboto", 20, "bold")).pack(pady=10)

        Button(self.parent, text="Add Item", command=self.add_item).pack() # When one of these buttons is pressed it will run that corrosponding function
        Button(self.parent, text="View Items", command=self.view_items).pack()
        Button(self.parent, text="Search", command=self.search_screen).pack()


    def add_item(self):
        self.clear_screen()

        Label(self.parent, text="Add Item").pack()

        Label(self.parent, text="Item Name:").pack()
        name_entry = Entry(self.parent)
        name_entry.pack()

        Label(self.parent, text="Price:").pack()
        price_entry = Entry(self.parent)
        price_entry.pack()

        Label(self.parent, text="Category:").pack()
        category_entry = Entry(self.parent)
        category_entry.pack()
        
        Label(self.parent, text="Stock:").pack()
        stock_entry = Entry(self.parent)
        stock_entry.pack()


        def save_item(): # Save function for the products
            name = name_entry.get() # Takes the text from and entry boxes and comes as a string, this include the numebrs
            price = price_entry.get()
            category = category_entry.get()
            stock = stock_entry.get()

            if name == "" or price == "" or category == "" or stock == "": # Checks if the user didnt input in a category and will make them enter the data again if data is missing
                print("Please fill out all fields")
                return

            price = float(price) # Converts strings to numbers, changes numbers written to int, allows the code to work correctly later
            stock = int(stock)

            new_item = Items(name, price, category, stock) # Creates a new object using the items class
            self.products_list.append(new_item) # Stores all of the items added into the inventory tracker

            print("Item Added")

        Button(self.parent, text="Save Item", command=save_item).pack()

        Button(self.parent, text="Back", command=self.main_menu).pack()


    def view_items(self):
        self.clear_screen()

        Label(self.parent, text="All Items").pack()

        for item in self.products_list: # The loop goes through the stored items one by one 
            text = item.name + " | $" + str(item.price) + " | " + item.category + " | Stock: " + str(item.stock) # This creates a string which shows all of the items info, str will convert the numbers back into text which allows for correct display
            Label(self.parent, text=text).pack()

        Button(self.parent, text="Back", command=self.main_menu).pack()


    def search_screen(self):
        self.clear_screen()

        Label(self.parent, text="Search by product name").pack()

        search_entry = Entry(self.parent)
        search_entry.pack()

        def search():
            keyword = search_entry.get().lower() # Makes the user's entered text lower case so when searching for a item it wont matter if the user users capital letters or not
            found = False # This is used to see if there is a match found when going through the loop

            for item in self.products_list: # Loops through all stored item
                if item.name.lower() == keyword:
                    print("Found:", item.name)
                    found = True # If the user enters the product and its there, it will print the "Found:"

            if found == False:
                print("No item in inventory") # If the loop doesn't match anything it will be false and print this

        Button(self.parent, text="Search", command=search).pack()

        Button(self.parent, text="Back", command=self.main_menu).pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Tracker")
    app = Inventory(root)
    root.geometry("400x600")
    root.configure(bg='green')
    root.mainloop()