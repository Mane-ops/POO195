from tkinter import messagebox
import math


class Controlador:
    def sumar(self, numero1, numero2):
        resultado = numero1 + numero2
        return messagebox.showinfo("Resultado",f"El resultado es {resultado}")
    
    def restar(self, numero1, numero2):
        resultado = numero1 - numero2
        return messagebox.showinfo("Resultado",f"El resultado es {resultado}")
    
    def multiplicar(self, numero1, numero2):
        try:
            resultado = numero1 * numero2
            return messagebox.showinfo("Resultado",f"El resultado es {resultado}")
        except OverflowError:
            return messagebox.showerror("Error","El numero es demasiado grande")
    
    def dividir(self, numero1, numero2):
        if numero2 == 0:
            return messagebox.showerror("Error","Imposible dividir entre 0")
        else:
            try:
                resultado = numero1 / numero2
                return messagebox.showinfo("Resultado",f"El resultado es {resultado}")
            except OverflowError:
                return messagebox.showerror("Error","El numero es demasiado grande")