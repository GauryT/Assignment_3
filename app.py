from tkinter import StringVar, font, ttk
from tkinter.constants import CENTER, W, E, N, S
from model import Model
import tkinter as tk

# Class definition (Encapsulation and Abstraction)
class Aplicacion(Model):
    def __init__(self, window):
        super().__init__()
        # Instance variable initialization
        self.window = window

        # Tkinter window setup
        self.window.title("Electronic Equipment Management")
        icon = tk.PhotoImage(file='logo.png')
        self.window.iconphoto(True, icon)
        self.window.configure(padx=20, pady=20)

        # Button style configuration using ttk.Style (Encapsulation)
        self.btn_style = ttk.Style().configure(
            "TButton", padding=6, background="#5E503F", foreground="#bf6d0a", font=("Century Gothic", 12, 'bold'))

        # Title label setup
        label = tk.Label(self.window,
                         text="Welcome to the product management system",
                         font=('Century Gothic', 16, 'bold'),
                         padx=20,
                         image=icon,
                         compound='top',
                         )
        label.grid(row=0, column=0, columnspan=5, pady=(0, 20))
        label.configure(anchor=CENTER)

        # Button for registering a new product
        btn = ttk.Button(self.window, text="Register New",
                         command=self.getAll, style=self.btn_style)
        btn.grid(row=1, column=0, columnspan=5)

        # Main Tkinter event loop
        self.window.mainloop()

    # Method demonstrating Inheritance
    def getAll(self):
        # Destroy the current window
        self.window.destroy()

        # Create a new window for the list of products
        self.window_list = tk.Tk()
        self.window_list.title("Product management")
        self.window_list.configure(padx=20, pady=20)

        # Label for the list of products
        self.modal_list_title = tk.Label(self.window_list, text="List of Products", font=("Century Gothic", 14, 'bold'))
        self.modal_list_title.grid(row=0, column=0, columnspan=4)

        # Button for adding a new product
        btn_add = ttk.Button(
            self.window_list, text="Add new", command=self.modalAdd, style=self.btn_style)
        btn_add.grid(row=1, column=0, columnspan=4)

        # Table headers
        thead_data = ['ID', 'NAME', 'QUANTITY', 'PRICE']
        h = 0
        self.table = ttk.Treeview(columns=("#1", "#2", "#3"), height=10)
        for j in thead_data:
            self.table.grid(row=2, column=h)
            self.table.heading('#{}'.format(h), text=j, anchor=CENTER)
            h += 1

        # Retrieve and display data in the table
        self.get()

        # Buttons for editing and deleting products
        self.btn_edit = ttk.Button(
            self.window_list, text="EDIT", command=self.modalEdit)
        self.btn_edit.grid(row=3, column=0, columnspan=4, sticky=W+E)
        self.btn_delete = ttk.Button(
            self.window_list, text="DELETE", command=self.deleteProduct)
        self.btn_delete.grid(row=4, column=0, columnspan=4, sticky=W+E)

        # Main Tkinter event loop for the new window
        self.window_list.mainloop()

    # Method demonstrating Polymorphism
    def get(self):
        # Table body
        records = self.table.get_children()
        for element in records:
            self.table.delete(element)
        # Retrieve data from the Model class and populate the table
        datos = Model().select()
        for i in datos:
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))

    # Method demonstrating Encapsulation
    def addProduct(self):
        # Add a new product using the Model class
        self.add(self.product_name.get(), self.product_cant.get(),
                 self.product_price.get())
        # Close the add product window and refresh the table
        self.window_add.destroy()
        self.get()

    # Method demonstrating Encapsulation
    def modalAdd(self):
        # Create a new window for adding a product
        self.window_add = tk.Toplevel()
        self.window_add.title("ADD NEW PRODUCT")
        self.window_add.configure(padx=20, pady=20)
        self.modal_add_label = ttk.Label(
            self.window_add, text="Add a product", font=("Century Gothic", 14, 'bold'))
        self.modal_add_label.grid(row=0, column=1, columnspan=5)
        # Entry fields for product information
        self.product_name_label = ttk.Label(
            self.window_add, text="Name", width=20)
        self.product_name_label.grid(row=1, column=1, columnspan=2)
        self.product_name = ttk.Entry(self.window_add, width=40)
        self.product_name.grid(row=1, column=3, columnspan=3)
        self.product_cant_label = ttk.Label(
            self.window_add, text="Quantity", width=20)
        self.product_cant_label.grid(row=2, column=1, columnspan=2)
        self.product_cant = ttk.Entry(self.window_add, width=40)
        self.product_cant.grid(row=2, column=3, columnspan=3)
        self.product_price_label = ttk.Label(
            self.window_add, text="Price", width=20)
        self.product_price_label.grid(row=3, column=1, columnspan=2)
        self.product_price = ttk.Entry(self.window_add, width=40)
        self.product_price.grid(row=3, column=3, columnspan=3)
        # Button for registering a new product
        self.btn_add_product = ttk.Button(
            self.window_add, text="Register Product", command=self.addProduct)
        self.btn_add_product.grid(row=4, column=1, columnspan=5)
        # Main Tkinter event loop for the new window
        self.window_add.mainloop()

    # Method demonstrating Encapsulation
    def edit(self):
        # Retrieve information from entry fields
        cod = self.product_id.get()
        name = self.product_name.get()
        cant = self.product_cant.get()
        price = self.product_price.get()
        # Update the product using the Model class
        self.update(name, cant, price, cod)
        # Close the edit product window and refresh the table
        self.window_edit.destroy()
        self.get()

    # Method demonstrating Encapsulation
    def modalEdit(self):
        # Retrieve information from the selected row in the table
        cod = self.table.item(self.table.selection())['text']
        name = self.table.item(self.table.selection())['values'][0]
        cant = self.table.item(self.table.selection())['values'][1]
        price = self.table.item(self.table.selection())['values'][2]
        # Create a new window for editing a product
        self.window_edit = tk.Toplevel()
        self.window_edit.title("Edit Products")
        self.window_edit.configure(padx=20, pady=20)
        self.modal_edit_label = ttk.Label(
            self.window_edit, text="Product Edit", font=("Century Gothic", 14, 'bold'))
        self.modal_edit_label.grid(row=0, column=0, columnspan=2)
        # Entry fields for product information
        self.product_id_label = tk.Label(self.window_edit, text="Id")
        self.product_id_label.grid(row=1, column=0)
        self.product_id = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=cod), state='readonly', width=30)
        self.product_id.grid(row=1, column=1)
        self.product_name_label = tk.Label(self.window_edit, text="Name")
        self.product_name_label.grid(row=2, column=0)
        self.product_name = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=name), width=30)
        self.product_name.grid(row=2, column=1)
        self.product_cant_label = tk.Label(self.window_edit, text="Quantity")
        self.product_cant_label.grid(row=3, column=0)
        self.product_cant = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=cant), width=30)
        self.product_cant.grid(row=3, column=1)
        self.product_price_label = tk.Label(self.window_edit, text="Amount")
        self.product_price_label.grid(row=4, column=0)
        self.product_price = tk.Entry(self.window_edit, textvariable=StringVar(
            self.window_edit, value=price), width=30)
        self.product_price.grid(row=4, column=1)
        # Button for saving the edited product
        self.btn = ttk.Button(
            self.window_edit, text="Save", command=self.edit).grid(row=5, column=0, columnspan=2)
        # Main Tkinter event loop for the new window
        self.window_edit.mainloop()

    # Method demonstrating Encapsulation
    def deleteProduct(self):
        # Delete the selected product using the Model class
        self.delete(self.table.item(self.table.selection())['text'])
        # Refresh the table
        self.get()


if __name__ == '__main__':
    window = tk.Tk()
    app = Aplicacion(window)
