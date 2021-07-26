from tkinter import *
from registro import *
from venta import *
root = Tk()
root.title("Tienda Fiusha")
root.geometry("300x300")

def registro():
    ventana_registro=Tk()
    registro_ventana =Registro (ventana_registro)
    ventana_registro.mainloop()

def venta():
    ventana_venta=Tk()
    venta_ventana= Venta(ventana_venta)
    ventana_venta.mainloop()

 # Menu 1
menu1 = Menu(root)
root.config(menu=menu1)
sub_menu = Menu(menu1)
menu1.add_cascade(menu=sub_menu, label="Opciones")
sub_menu.add_command(label="Registros", command=registro)
sub_menu.add_command(label="Ventas", command=venta)   

root.mainloop()