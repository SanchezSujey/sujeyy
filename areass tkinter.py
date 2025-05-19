import tkinter as tk
from tkinter import messagebox
import math

def mostrar_formula():
    figura = opcion.get()
    for widget in frame_datos.winfo_children():
        widget.destroy()

    if figura == "Triángulo":
        tk.Label(frame_datos, text="Fórmula: Área = (base × altura) / 2").pack()
        tk.Label(frame_datos, text="Base:").pack()
        entradas["base"] = tk.Entry(frame_datos)
        entradas["base"].pack()
        tk.Label(frame_datos, text="Altura:").pack()
        entradas["altura"] = tk.Entry(frame_datos)
        entradas["altura"].pack()
    elif figura == "Rectángulo":
        tk.Label(frame_datos, text="Fórmula: Área = base × altura").pack()
        tk.Label(frame_datos, text="Base:").pack()
        entradas["base"] = tk.Entry(frame_datos)
        entradas["base"].pack()
        tk.Label(frame_datos, text="Altura:").pack()
        entradas["altura"] = tk.Entry(frame_datos)
        entradas["altura"].pack()
    elif figura == "Cuadrado":
        tk.Label(frame_datos, text="Fórmula: Área = lado × lado").pack()
        tk.Label(frame_datos, text="Lado:").pack()
        entradas["lado"] = tk.Entry(frame_datos)
        entradas["lado"].pack()
    elif figura == "Círculo":
        tk.Label(frame_datos, text="Fórmula: Área = 3.1416 × radio²").pack()
        tk.Label(frame_datos, text="Radio:").pack()
        entradas["radio"] = tk.Entry(frame_datos)
        entradas["radio"].pack()

    tk.Button(frame_datos, text="Calcular área", command=calcular_area).pack(pady=10)

def calcular_area():
    figura = opcion.get()
    try:
        if figura == "Triángulo":
            base = float(entradas["base"].get())
            altura = float(entradas["altura"].get())
            area = (base * altura) / 2
        elif figura == "Rectángulo":
            base = float(entradas["base"].get())
            altura = float(entradas["altura"].get())
            area = base * altura
        elif figura == "Cuadrado":
            lado = float(entradas["lado"].get())
            area = lado * lado
        elif figura == "Círculo":
            radio = float(entradas["radio"].get())
            area = math.pi * (radio ** 2)
        else:
            area = 0

        messagebox.showinfo("Resultado", f"Área del {figura.lower()}: {round(area, 2)}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Interfaz
ventana = tk.Tk()
ventana.title("Cálculo de Áreas")
ventana.geometry("500x400")

tk.Label(ventana, text="Selecciona una figura:").pack()

opcion = tk.StringVar(value="Triángulo")
entradas = {}

# RadioButtons
figuras = ["Triángulo", "Rectángulo", "Cuadrado", "Círculo"]
for fig in figuras:
    tk.Radiobutton(ventana, text=fig, variable=opcion, value=fig).pack(anchor="w")

tk.Button(ventana, text="Mostrar fórmula", command=mostrar_formula).pack(pady=10)

frame_datos = tk.Frame(ventana)
frame_datos.pack()

ventana.mainloop()