# main.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def despedir(nombre):
    print(f"Adiós, {nombre}!")  # Nueva función

if __name__ == "__main__":
    saludar("Mundo")
    despedir("Mundo")  # Llamada a la nueva función
