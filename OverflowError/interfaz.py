import tkinter
from controlador import *

Objnum = Controlador()

def click_sumar():
    num1 = float(e_num1.get())
    num2 = float(e_num2.get())
    Objnum.sumar(num1,num2)

def click_restar():
    num1 = float(e_num1.get())
    num2 = float(e_num2.get())
    Objnum.restar(num1,num2)

def click_multiplicar():
    num1 = float(e_num1.get())
    num2 = float(e_num2.get())
    Objnum.multiplicar(num1,num2)

def click_dividir():
    num1 = float(e_num1.get())
    num2 = float(e_num2.get())
    Objnum.dividir(num1,num2)

ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("+400+180")

label_titulo = tkinter.Label(ventana, text="Calculadora", font=("Arial", 25))
label_num1 = tkinter.Label(ventana, text="Primer Número", font=("Arial", 12))
label_num2 = tkinter.Label(ventana, text="Segundo Número", font=("Arial", 12))

e_num1 = tkinter.Entry(ventana, font=("Arial", 15))
e_num2 = tkinter.Entry(ventana, font=("Arial", 15))

boton_suma = tkinter.Button(ventana, text="Sumar", bg="black", fg="white", font="Arial 12", width=25, command=click_sumar)
boton_resta = tkinter.Button(ventana, text="Restar", bg="black", fg="white", font="Arial 12", width=25, command=click_restar)
boton_multiplicacion = tkinter.Button(ventana, text="Multiplicar", bg="black", fg="white", font="Arial 12", width=25, command=click_multiplicar)
boton_division = tkinter.Button(ventana, text="Dividir", bg="black", fg="white", font="Arial 12", width=25, command=click_dividir)

label_titulo.grid(row=0, column=0, columnspan=2, pady=8)
label_num1.grid(row=1, column=0, pady=5)
label_num2.grid(row=2, column=0)
e_num1.grid(row=1, column=1, pady=8)
e_num2.grid(row=2, column=1)

boton_suma.grid(row=3, column=0, columnspan=2, pady=10)
boton_resta.grid(row=4, column=0, columnspan=2, pady=5)
boton_multiplicacion.grid(row=5, column=0, columnspan=2, pady=5)
boton_division.grid(row=6, column=0, columnspan=2, pady=5)

label_resultado = tkinter.Label(ventana)
label_resultado.grid(row=7, column=0, columnspan=2)

ventana.mainloop()