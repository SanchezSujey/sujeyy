import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

datos_guardados = []
def pantalla_uno():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="bienvenido al inicio", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="ventana", command=lambda: messagebox.showinfo("Holaa", ":)")).pack()

def pantalla_dos():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Datos a guardar", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Ingresa el nombre del alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Seleccione el genero:").pack()
    opcion_elegida = tk.StringVar(value="Masculino")
    tk.Radiobutton(area_dinamica, text="Masculino", variable=opcion_elegida, value="Masculino").pack()
    tk.Radiobutton(area_dinamica, text="Femenino", variable=opcion_elegida, value="Femenino").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["diez", "nueve", "ocho"])
    combo.pack()
    combo.current(0)

    etiqueta_datos = tk.Label(area_dinamica, text="", font=("Arial", 12), fg="black", justify="left")
    etiqueta_datos.pack(pady=10)

    def accion_guardar():
        valor = campo_texto_uno.get()
        seleccion = opcion_elegida.get()
        lista = combo.get()
        dato_formateado = f"Nombre: {valor}, Genero: {seleccion}, Cal: {lista}"
        datos_guardados.append(dato_formateado)
        etiqueta_datos.config(text="\n".join(datos_guardados))
        campo_texto_uno.delete(0, tk.END)


    tk.Button(area_dinamica, text="guardar datos", command=accion_guardar).pack(pady=10)


def pantalla_tres():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def pantalla_cuatro():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("500x400") 
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white") 
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Pantalla de inicio", command=pantalla_uno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ingresar datos", command=pantalla_dos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cambio de color", command=pantalla_tres, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Preguntas", command=pantalla_cuatro, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

pantalla_uno()
ventana_principal.mainloop()