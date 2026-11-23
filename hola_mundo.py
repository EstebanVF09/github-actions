import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Este es el archivo hola_mundo!")
    print(f"¡Hola, {nombre} desde GitHub Actions y Python!")

if __name__ == "__main__":
    main()