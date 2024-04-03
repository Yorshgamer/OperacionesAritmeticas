def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_of_three_numbers(a, b, c):
    return gcd(a, gcd(b, c))

# Función para solicitar al usuario un número positivo
def solicitar_numero(mensaje):
    while True:
        num = int(input(mensaje))
        if num > 0:
            return num
        else:
            print("Por favor, ingresa un número positivo.")

# Solicitar al usuario que ingrese los tres números
num1 = solicitar_numero("Ingresa el primer número: ")
num2 = solicitar_numero("Ingresa el segundo número: ")
num3 = solicitar_numero("Ingresa el tercer número: ")

# Calcular el máximo común divisor de los tres números
resultado = gcd_of_three_numbers(num1, num2, num3)
print("El máximo común divisor de", num1, ",", num2, "y", num3, "es:", resultado)

