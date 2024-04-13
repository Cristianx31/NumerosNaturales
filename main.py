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

    def calcular_mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo (MCM) de dos números utilizando el MCD.

        Args:
            a (int): El primer número.
            b (int): El segundo número.

        Returns:
            int: El mínimo común múltiplo de a y b.
        """
        mcd = self.calcular_mcd(a, b)
        mcm = (a * b) // mcd
        return mcm


# Pedir al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Calcular el MCD y el MCM
mcd = calculadora.calcular_mcd(num1, num2)
mcm = calculadora.calcular_mcm(num1, num2)

# Mostrar el MCD y el MCM
print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")
print(f"El mínimo común múltiplo de {num1} y {num2} es: {mcm}")
