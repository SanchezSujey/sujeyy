import tkinter as tk
from tkinter import messagebox


class AplicacionSuma:
    def __init__(self, master):
        self.master = master
        self.master.title("Suma de dos números")

        
        tk.Label(master, text="Primer número:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(master, text="Segundo número:").grid(row=1, column=0, padx=10, pady=10)

        
        self.entrada1 = tk.Entry(master)
        self.entrada2 = tk.Entry(master)
        self.entrada1.grid(row=0, column=1)
        self.entrada2.grid(row=1, column=1)

        
        self.boton_sumar = tk.Button(master, text="Sumar", command=self.calcular_suma)
        self.boton_sumar.grid(row=2, column=0, columnspan=2, pady=10)

        self.resultado = tk.Label(master, text="Resultado: ")
        self.resultado.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_suma(self):
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            suma = num1 + num2
            self.resultado.config(text=f"Resultado: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionSuma(ventana)
    ventana.mainloop()