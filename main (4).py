import tkinter as tk 

def saludar():
    nombre = entrada.get() 
    etiqueta_resultado.config(text=f"Hola {nombre}",tienes {edad} año") 

    

    ventana = tk.Tk() 
    ventana.title("Saludo") 
   ventana.title("edad")
    ventana.geometry("300x150") 

    etiqueta = tk.Label(ventana, text="Ingresa tu nombre:") 
    etiqueta.pack() 
   
    etiqueta = tk.Label(ventana, text="Ingresa tu edad:") 
    etiqueta.pack()

    entrada = tk.Entry(ventana) 
    entrada.pack() 

    boton = tk.Button(ventana, text="Saludar", command=saludar) 
    boton.pack() 
  boton = tk.Button(ventana, mostrar="edad", command=mostrar_edad)    
  boton.pack() 

    etiqueta_resultado = tk.Label(ventana, text="") 
    etiqueta_resultado.pack() 

    ventana.mainloop() 
