class Suma:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def leer_datos(self):
        try:
            self.num1 = float(input("Ingrese el primer número: "))
            self.num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Entrada no válida. Intenta nuevamente.")
            self.leer_datos()

    def calcular_suma(self):
        return self.num1 + self.num2

    def mostrar_resultado(self):
        resultado = self.calcular_suma()
        print(f"La suma de {self.num1} y {self.num2} es: {resultado}")


def main():
    print("Programa orientado a objetos que suma dos números\n")
    operacion = Suma()
    operacion.leer_datos()
    operacion.mostrar_resultado()

if __name__ == "__main__":
    main()