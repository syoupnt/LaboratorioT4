print("MANIPULACION Y BUSQUEDA DE DATOS\n")

# 3. Manipular cadenas de texto
texto = "FUNDAMENTOS DE PROGRAMACIÓN"
print("1. MANIPULACION DE CADENAS")
print(f"Texto original: {texto}")

subcadena = texto[0:12]
posicion = texto.find("PROGRAMACIÓN")
texto_reemplazado = texto.replace("PROGRAMACIÓN", "INFORMÁTICA")
palabras = texto.split()

print(f"Subcadena (posiciones 0 a 11): {subcadena}")
print(f"Posición de la palabra 'PROGRAMACIÓN': {posicion}")
print(f"Texto con reemplazo: {texto_reemplazado}")
print(f"Texto separado en palabras: {palabras}\n")

# 4. Implementar listas paralelas
nombres = ["Ana", "Luis", "Maria", "Carlos"]
edades = [20, 22, 19, 21]
nombre_buscado = "Maria"

print("2. LISTAS PARALELAS")
print(f"Nombres: {nombres}")
print(f"Edades:  {edades}")

i = 0
for nombre in nombres:
    if nombre == nombre_buscado:
        print(f"{nombre_buscado} tiene {edades[i]} años.")
        break
    i += 1

# 5. Construir una estructura combinada
usuarios = [
    {"nombre": "Ana", "email": "ana@gmail.com", "ciudad": "Lima"},
    {"nombre": "Luis", "email": "luis@gmail.com", "ciudad": "Quito"},
    {"nombre": "Maria", "email": "maria@gmail.com", "ciudad": "Quito"},
    {"nombre": "Carlos", "email": "carlos@gmail.com", "ciudad": "Lima"},
]
ciudad_buscada = "Quito"

# 6. Realizar una busqueda por ciudad
print("\n3. BUSQUEDA EN LA ESTRUCTURA COMBINADA")
print(f"Usuarios registrados: {usuarios}")
print(f"Personas que viven en {ciudad_buscada}:")

for usuario in usuarios:
    if usuario["ciudad"] == ciudad_buscada:
        print(
            f"- {usuario['nombre']} | {usuario['email']} | {usuario['ciudad']}"
        )

# 7. Ordenar alfabeticamente los nombres de los usuarios
nombres = []
for usuario in usuarios:
    nombres.append(usuario["nombre"])

nombres_ordenados = sorted(nombres)

print("\n4. NOMBRES ORDENADOS ALFABETICAMENTE")
print(nombres_ordenados)
