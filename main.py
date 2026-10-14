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
