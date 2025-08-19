import os

# Funcion Hola Mundo
def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")


if __name__ == "__main__":
    main()