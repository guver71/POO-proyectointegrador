from tkinter import *
import tkinter
import md5
from tkinter import tkMessageBox

ventana = Tk()
ventana.title("----------Login Master v0.1-------------")
ventana.geometry("320x80+500+250")
ventana.resizable(width="FALSE",height="FALSE")
Label(ventana,text="User").pack()
caja = Entry(ventana)
caja.pack()
s = StringVar()
margen = 0
def codificar(x):
 f = md5.new()
 f.update(x)
 return f.hexdigest()
Label(ventana,textvar=s).pack()
def logear():
 a=caja.get()
 if a == "":
  showerror(title="Error",message="Inserte texto en el campo")
 else:
  logear2()
def logear2():
 a=caja.get()
 m=codificar(a)
 if m == "b8f002559f4cfc740db2de36535cac6b":
  s = "Logeo completado, Bienvenido "+ a + " :)"
  showinfo(title="Bien",message=s)
 else:
  showerror(title="Mal",message="ERROR DE LOGEO")
Button(ventana,text="Logear",command=logear).pack()

ventana.mainloop()
  