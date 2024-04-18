import os

# Limpia la consola al inicio del programa
os.system('cls' if os.name == 'nt' else 'clear')

# Lista para almacenar los candidatos
candidatos = []

def clear_console():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_candidato(candidato):
    """Valida si un candidato cumple con los requisitos"""
    edad_valida = 25 <= candidato['edad'] <= 35
    experiencia_valida = 2 <= candidato['experiencia'] <= 4
    return edad_valida and experiencia_valida

def registrar_candidato():
    """Registra un nuevo candidato"""
    clear_console()
    print("=== Registrar Candidato ===")
    nombre = input("Nombre completo: ")
    identificacion = input("Identificacion: ")
    correo = input("Correo electronico: ")
    contacto = input("Contacto: ")
    edad = int(input("Edad: "))
    experiencia = int(input("Años de experiencia: "))
    print("Profesion:")
    print("1. Ingenieria en sistemas")
    print("2. Ingenieria informatica")
    profesion_opcion = input("Selecciona una opcion (1 o 2): ")
    profesion = ""
    if profesion_opcion == "1":
        profesion = "Ingenieria en sistemas"
    elif profesion_opcion == "2":
        profesion = "Ingenieria informatica"
    else:
        print("Opcion no valida. Se asumira Ingenieria en sistemas.")
        profesion = "Ingenieria en sistemas"

    ciudad = input("Ciudad: ")
    sexo = input("Sexo: ")

    candidato = {
        'nombre': nombre,
        'identificacion': identificacion,
        'correo': correo,
        'contacto': contacto,
        'edad': edad,
        'experiencia': experiencia,
        'profesion': profesion,
        'ciudad': ciudad,
        'sexo': sexo
    }

    if validar_candidato(candidato):
        candidatos.append(candidato)
        print("Candidato registrado exitosamente.")
    else:
        print("El candidato no cumple con los requisitos.")

    input("Presiona Enter para continuar...")
    clear_console()

def consultar_candidatos():
    """Muestra todos los candidatos registrados"""
    clear_console()
    print("=== Candidatos Registrados ===")
    if candidatos:
        for idx, candidato in enumerate(candidatos, start=1):
            print(f"Candidato {idx}:")
            for key, value in candidato.items():
                print(f"{key.capitalize()}: {value}")
            print("-" * 20)
    else:
        print("No hay candidatos registrados.")

    input("Presiona Enter para continuar...")
    clear_console()

def menu():
    """Muestra el menu de opciones"""
    while True:
        print("=== Menu ===")
        print("1. Registrar Candidato")
        print("2. Consultar Candidatos")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            registrar_candidato()
        elif opcion == "2":
            consultar_candidatos()
        elif opcion == "3":
            clear_console()
            print("Chao bro")
            break
        else:
            clear_console()
            print("Opción no valida. Intentalo de nuevo.")

if __name__ == "__main__":
    menu()
