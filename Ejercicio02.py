import csv
import random
import string
import cProfile

# Función para capitalizar el nombre
def capitalizar_nombre(nombre):
    return nombre.strip().title()

# Función para calcular la letra del DNI español
def calcular_letra_dni(dni_numero):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[dni_numero % 23]

# Función para leer los archivos CSV
def leer_fichero_csv(nombre_fichero):
    personas = []
    with open(nombre_fichero, mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for fila in lector:
            if fila:  # Evitar líneas vacías
                personas.append(fila[0])  # Suponemos que el nombre está en la primera columna
    return personas

# Función que procesa las personas
def procesar_personas(nombre_fichero):
    personas = leer_fichero_csv(nombre_fichero)
    resultados = []
    for persona in personas:
        nombre_capitalizado = capitalizar_nombre(persona)
        dni_numero = random.randint(10000000, 99999999)  # Generamos un número de DNI aleatorio
        letra_dni = calcular_letra_dni(dni_numero)
        resultados.append((nombre_capitalizado, dni_numero, letra_dni))
    return resultados

# Función para realizar la comprobación de rendimiento con cProfile
def medir_rendimiento():
    # Medir el rendimiento de procesar 50 personas
    print("Medición de rendimiento para 50 personas:")
    cProfile.run('procesar_personas("personas_50.csv")')

    # Medir el rendimiento de procesar 1000 personas
    print("\nMedición de rendimiento para 1000 personas:")
    cProfile.run('procesar_personas("personas_1000.csv")')

# Generar un archivo CSV con nombres aleatorios para las pruebas
def generar_archivo_csv(nombre_archivo, num_personas):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        for _ in range(num_personas):
            nombre_aleatorio = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
            escritor.writerow([nombre_aleatorio])

# Generar los archivos para las pruebas (solo una vez)
generar_archivo_csv("personas_50.csv", 50)
generar_archivo_csv("personas_1000.csv", 1000)

# Ejecutar la medición de rendimiento
if __name__ == "__main__":
    medir_rendimiento()

	
