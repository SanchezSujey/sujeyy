import tkinter as tk

def sumar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado.config(text=f"Resultado de la suma: {num1+num2}")
  
  
def restar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado.config(text=f"Resultado de la resta: {num1-num2}")
   
ventana = tk.Tk()
ventana.title("Operaciones")
ventana.geometry("300x300")



etiqueta1 = tk.Label(ventana, text="Ingresa el numero 1:")
etiqueta1.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta2 = tk.Label(ventana, text="Ingresa el numero 2:")
etiqueta2.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana.config(bg="black"),text="suma",command=sumar)
boton.pack()



boton = tk.Button(ventana, text="Resta", command=restar)
boton.pack()



resultado = tk.Label(ventana, text="")
resultado.pack()


ventana.mainloop()