"""
Licencia: Apache
Organización: UNIR
Descripción: Este script lee una lista de palabras desde un archivo, opcionalmente elimina duplicados, y las ordena.
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def ordenar_lista(items, ascendente=True):

    if not isinstance(items, list):
        raise TypeError(f"No se puede ordenar un objeto de tipo {type(items)}. Se requiere una lista.")

    return sorted(items, reverse=not ascendente)


def eliminar_duplicados_de_lista(items):

    return list(set(items))


def leer_palabras_desde_archivo(filename):
    if not os.path.isfile(filename):
        print(f"El archivo '{filename}' no se encontró. Usando la lista de palabras predeterminada.")
        return ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def main():
    filename = DEFAULT_FILENAME
    eliminar_duplicados = DEFAULT_DUPLICATES

    if len(sys.argv) == 3:
        filename = sys.argv[1]
        eliminar_duplicados = sys.argv[2].strip().lower() == "yes"
    else:
        print("Uso: python script.py <nombre_archivo> <eliminar_duplicados>")
        print("  <nombre_archivo>: Nombre del archivo que contiene las palabras.")
        print("  <eliminar_duplicados>: 'yes' para eliminar duplicados, 'no' en caso contrario.")
        sys.exit(1)

    print(f"Leyendo palabras del archivo: '{filename}'")
    lista_palabras = leer_palabras_desde_archivo(filename)

    if eliminar_duplicados:
        print("Eliminando duplicados...")
        lista_palabras = eliminar_duplicados_de_lista(lista_palabras)

    palabras_ordenadas = ordenar_lista(lista_palabras)
    print("Palabras ordenadas:", palabras_ordenadas)


if __name__ == "__main__":
    main()
