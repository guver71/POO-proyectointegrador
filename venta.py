from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3

class Venta:

    db = "database.db"

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("700x900")
        self.ventana.title("Ventas")
        
        frame = LabelFrame(self.ventana, text="Ventas")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        ttk.Button(frame, text="Nuevo", command=self.new_venta).grid(row=0, column=0)
        frame_options = LabelFrame(frame, text="Ingresar producto")
        frame_options.grid(row=0, column=0, sticky = W + E)

        ttk.Button(frame_options, text="Nuevo", command=self.new_venta).grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Eliminar", command=self.delete).grid(row=1, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Cerrar", command=self.close).grid(row=2, column=0, sticky = W + E)

        self.table = ttk.Treeview(frame, height=20,  columns=("producto", "talla","color", "precio", "nombre_cliente"))
        self.table.grid(row=0, column=3)
        self.table.heading('#0', text='ID')
        self.table.heading('producto', text='Producto')
        self.table.heading('talla', text='Talla')
        self.table.heading('color', text='Correo')
        self.table.heading('precio', text='Precio')
        self.table.heading('nombre_cliente', text='Nombre_cliente')
        self.get_venta()

    def new_venta(self):
        self.new_ventana = Toplevel()
        self.new_ventana.title = 'Nueva Venta'
        Label(self.new_ventana, text = 'Producto:').grid(row = 0, column = 1)
        producto = Entry(self.new_ventana)
        producto.grid(row = 0, column = 2)
        Label(self.new_ventana, text = 'Talla:').grid(row = 1, column = 1)
        talla = Entry(self.new_ventana)
        talla.grid(row = 1, column = 2)
        Label(self.new_ventana, text = 'Color:').grid(row = 2, column = 1)
        color= Entry(self.new_ventana)
        color.grid(row = 2, column = 2)
        Label(self.new_ventana, text = 'Nombre_Cliente:').grid(row = 3, column = 1)
        nombre_cliente= Entry(self.new_ventana)
        nombre_cliente.grid(row = 3, column = 2)
        Button(self.new_ventana, text = 'Guardar', command = lambda: self.save_venta(producto.get(),  talla.get(), color.get(), nombre_cliente.get())).grid(row = 5, column = 2, sticky = W)
        self.new_ventana.mainloop()

    def get_venta(self):
        list = self.table.get_children()
        for item in list:
            self.table.delete(item)

        query = 'SELECT * FROM venta'
        rows = self.query(query)
        for row in rows:
            self.table.insert(parent='', index=row[0], iid=row[0], text=row[0], values=(row[1], row[2], row[3]))

    def save_product(self, producto, talla, color, nombre_cliente):
        query = 'INSERT INTO venta VALUES(NULL,?,?,?,?)'
        params = (producto, talla, color, nombre_cliente)
        self.query(query, params)
        self.new_ventana.destroy()
        self.get_venta()

    def close(self):
        self.window.destroy()
        return None

    def delete(self):
    
        try:
            self.table.item(self.table.selection())['text']
        except IndexError as e:
            print("error")
         
        id = self.table.item(self.table.selection())['text']
        query = 'DELETE FROM product WHERE id=?'
        self.query(query, (id,))
        self.get_venta()
      




  
