def preparar_datos(info):
     acumulador = ""
     for letra in info:
         acumulador += letra + "-"
     return acumulador[:-1]
     
def mezcla_datos(a,b):
          if a > b :
               return a+b
          elif a==b :
               return a*2
          else: 
               return b +a 
def iniciar():
        entrada1 = input("ingresa un valor de referencia textual:")
        entrada2 = input("ingresa otra unidad:")
        
        x = preparar_datos(entrada1)
        y = preparar_datos(entrada2)
       
        resultado = mezcla_datos(x,y) 
        print("resultado final:", resultado)
        
        if entrada1 in entrada2 :
            print("coincidencia detectada.")

iniciar()