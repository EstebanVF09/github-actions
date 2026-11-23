import os


def main():
    nombre = os.getenv("USERNAME")
    lenguaje = os.getenv("USERNAME")
    print(f"¡Este es el archivo hola_lenguaje!")
    print(f"¡Hola, {nombre} desde GitHub Actions y Python!")
    print(f"Este es tu lenguaje favorito, {lenguaje}!")

if __name__ == "__main__":
    main()