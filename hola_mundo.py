import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Este es el archivo hola_mundo!")
    print(f"¡Hola, {nombre} desde GitHub Actions y Python!")

def expresiones():
    usuario = os.getenv("USER")
    print(f"¡Hola, este usuario se enviar al registro via api {usuario} desde GitHub Actions y Python!")


if __name__ == "__main__":
    expresiones()