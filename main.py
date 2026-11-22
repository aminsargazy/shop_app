import tkinter as tk
from tkinter import messagebox
from shop import Product
from shop_manager import ShopManage


class ShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop App")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.manager = ShopManage("shop_products.json")
        self.selected_product = None
        self.widget()
        self.load_product()

    def widget(self):
        self.header = tk.Label(self.root, text="ShopApp", font=("Arial", 22))
        self.header.pack()

        self.name_label = tk.Label(self.root, text="Name product:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root, width=40, justify="center")
        self.name_entry.pack(pady=5)

        self.price_label = tk.Label(self.root, text="Price product:")
        self.price_label.pack()

        self.price_entry = tk.Entry(self.root, width=40, justify="center")
        self.price_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add", command=self.add_product)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_product)
        self.delete_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit", command=self.edit_product)
        self.edit_button.pack(pady=5)

        self.product_list = tk.Listbox(self.root, width=50, height=15)
        self.product_list.pack(pady=10)

        self.product_list.bind("<<ListboxSelect>>", self.select_product)

    def select_product(self, event):
        selection = self.product_list.curselection()

        if not selection:
            return

        index = selection[0]
        products = self.manager.show_all()
        self.selected_product = products[index]

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

        self.name_entry.insert(0, self.selected_product.name)
        self.price_entry.insert(0, self.selected_product.price)

    def load_product(self):
        self.product_list.delete(0, tk.END)
        products = self.manager.show_all()

        for product in products:
            self.product_list.insert(tk.END, f"{product.name} - {product.price}")

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.selected_product = None

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()

        if name == "" or price == "":
            messagebox.showwarning("Warning", "Fill all fields!")
            return

        product = Product(name, price)
        self.manager.add_product(product)

        self.load_product()
        self.clear_form()

    def delete_product(self):
        if self.selected_product is None:
            messagebox.showwarning("Warning", "Select product!")
            return

        self.manager.delete_product(self.selected_product.name)

        self.load_product()
        self.clear_form()

    def edit_product(self):
        if self.selected_product is None:
            messagebox.showwarning("Warning", "Select product!")
            return

        name = self.name_entry.get()
        price = self.price_entry.get()

        if name == "" or price == "":
            messagebox.showwarning("Warning", "Fill all fields!")
            return

        old_name = self.selected_product.name
        product = Product(name, price)

        self.manager.update(old_name, product)

        self.load_product()
        self.clear_form()


root = tk.Tk()
app = ShopApp(root)
root.mainloop()