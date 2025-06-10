class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        """Método para ingresar una temperatura diaria."""
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas ingresadas."""
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    clima = ClimaDiario()
    print("Bienvenido al programa de cálculo de promedio de temperaturas semanales.")
    
    for i in range(7):  # Ingresar temperaturas para 7 días
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima.ingresar_temperatura(temp)

    promedio = clima.calcular_promedio()
    print(f"La temperatura promedio semanal es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
