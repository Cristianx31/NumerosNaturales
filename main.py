class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        """
        Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.

        Args:
            a (int): El primer número.
            b (int): El segundo número.

        Returns:
            int: El máximo común divisor de a y b.
        """
        while b != 0:
            a, b = b, a % b
        return a

# Pedir al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Calcular y mostrar el MCD
mcd = calculadora.calcular_mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")

