class Suma:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def leer_datos(self):
        while True:
            try:
                self.num1 = float(input("Ingrese el primer número: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        while True:
            try:
                self.num2 = float(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número válido.")

    def calcular_suma(self):
        return self.num1 + self.num2

    def mostrar_resultado(self):
        resultado = self.calcular_suma()
        print(f"\nLa suma de {self.num1} y {self.num2} es: {resultado}")

4
if __name__ == "__main__":
    operacion = Suma()
    operacion.leer_datos()
    operacion.mostrar_resultado()