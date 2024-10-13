import os

def contarCaracteres(rutaArchivo):
    #Diccionario para el conteo de caracteres
    conteo = {}

    #Abrir el archivo
    with open(rutaArchivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

        # Recorrer caracteres
        for caracter in contenido:
            #Aumentar el conteo del caracter
            if caracter in conteo:
                conteo[caracter] += 1
            #Si el carácter no está en el diccionario, agregarlo por primera vez
            else:
                conteo[caracter] = 1

    return conteo

#Obtener el nombre del archivo desde el escritorio del usuario
def obtener_ruta_archivo():
    #Ruta del escritorio del usuario
    rutaDesktop = os.path.join(os.path.expanduser("~"), "Desktop")
    nombreArchivo = input("Ingresa el nombre del archivo .txt (sin la extensión, el archivo debe ubicarse en el escritorio): ") + ".txt"
    rutaArchivo = os.path.join(rutaDesktop, nombreArchivo)

    #Verificar que exista el archivo
    if not os.path.exists(rutaArchivo):
        print(f"El archivo '{nombreArchivo}' no se encuentra en el escritorio.")
        return None
    return rutaArchivo

def main():
    rutaArchivo = obtener_ruta_archivo()
    
    if rutaArchivo:
        conteo = contarCaracteres(rutaArchivo)
        print("\nConteo de caracteres en el archivo:")
        for caracter, cantidad in conteo.items():
            print(f"'{caracter}': {cantidad}")

if __name__ == "__main__":
    main()
