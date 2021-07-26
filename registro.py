from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkdocviewer import *

class Registro:

    db = "database.db"

    def __init__(self, ventana) :
        self.ventana = ventana
        self.ventana.geometry('800x800') 
        self.ventana.title('REGISTRO')

        frame = LabelFrame(self.ventana, text="Registro de vestimenta")
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        frame_options = LabelFrame(frame, text="Opciones")
        frame_options.grid(row=0, column=0, sticky = W + E)

        ttk.Button(frame_options, text="Nuevo", command=self.new_registro).grid(row=0, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Eliminar", command=self.delete).grid(row=1, column=0, sticky = W + E)
        ttk.Button(frame_options, text="Cerrar", command=self.close).grid(row=2, column=0, sticky = W + E)
       

        self.table = ttk.Treeview(frame, height=20,  columns=("producto", "talla","color", "precio"))
        self.table.grid(row=0, column=3)
        self.table.heading('#0', text='ID')
        self.table.heading('producto', text='Producto')
        self.table.heading('talla', text='Talla')
        self.table.heading('color', text='Color')
        self.table.heading('precio', text='Precio')
    
        self.get_registro()
    
    def new_registro(self):
        self.new_ventana = Toplevel()
        self.new_ventana.title = 'Nuevo Registro'
        Label(self.new_ventana, text = 'Producto:').grid(row = 0, column = 1)
        producto = Entry(self.new_ventana)
        producto.grid(row = 0, column = 2)
        Label(self.new_ventana, text = 'Talla:').grid(row = 1, column = 1)
        talla = Entry(self.new_ventana)
        talla.grid(row = 1, column = 2)
        Label(self.new_ventana, text = 'Color:').grid(row = 2, column = 1)
        color= Entry(self.new_ventana)
        color.grid(row = 2, column = 2)
        Label(self.new_ventana, text = 'Precio:').grid(row = 3, column = 1)
        precio= Entry(self.new_ventana)
        precio.grid(row = 3, column = 2)
        Button(self.new_ventana, text = 'Guardar Registro', command = lambda: self.save_registro(producto.get(),  talla.get(), color.get(), precio.get())).grid(row = 5, column = 2, sticky = W+E)

        self.new_ventana.mainloop()

    

    def save_registro(self, producto, talla, color, precio):
        query = 'INSERT INTO registro VALUES(NULL,?,?,?,?)'
        params = (producto, talla, color, precio)
        self.query(query, params)
        self.new_ventana.destroy()
        self.get_registro()

    def query(self, query, params=()):
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def get_registro(self):
        list = self.table.get_children()
        for item in list:
            self.table.delete(item)

        query = 'SELECT * FROM registro'
        rows = self.query(query)
        for row in rows:
            self.table.insert(parent='', index=row[0], iid=row[0], text=row[0], values=(row[1], row[2], row[3])) 

    def close(self):
        self.ventana.destroy()
        return None

    def delete(self):
    
        try:
            self.table.item(self.table.selection())['text']
        except IndexError as e:
            print("error")
            
        id = self.table.item(self.table.selection())['text']
        query = 'DELETE FROM registro WHERE id=?'
        self.query(query, (id,))
        self.get_registro()
       
    

  