import tkinter as tk
from tkinter import messagebox

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class CalcularArea:
    def __init__(self, root):
        self.root = root
        self.root.title("Área de un Triángulo")

        tk.Label(root, text="Base:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_base = tk.Entry(root)
        self.entry_base.grid(row=0, column=1, pady=5)

        tk.Label(root, text="Altura:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_altura = tk.Entry(root)
        self.entry_altura.grid(row=1, column=1, pady=5)

        self.boton_calcular = tk.Button(root, text="Calcular Área", command=self.calcular_area)
        self.boton_calcular.grid(row=2, column=0, columnspan=2, pady=10)

    def calcular_area(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())

            if base <= 0 or altura <= 0:
                raise ValueError("Los valores deben ser mayores a cero.")

            triangulo = Triangulo(base, altura)
            area = triangulo.calcular_area()

            messagebox.showinfo("Resultado", f"El área del triángulo es: {area:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalcularArea(root)
    root.mainloop()