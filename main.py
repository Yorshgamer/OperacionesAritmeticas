def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solicitar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            num = int(entrada)
            if num > 0:
                return num
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    num1 = solicitar_numero("Ingresa el primer número: ")
    num2 = solicitar_numero("Ingresa el segundo número: ")

    resultado = gcd(num1, num2)
    print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")

if __name__ == "__main__":
    main()
