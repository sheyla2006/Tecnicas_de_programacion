# Función para ingresar datos diarios de temperatura
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Ingresar temperaturas para 7 días
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal para ejecutar el programa
def main():
    print("Bienvenido al programa de cálculo de promedio de temperaturas semanales.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"La temperatura promedio semanal es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
