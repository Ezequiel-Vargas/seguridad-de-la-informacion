import hashlib
import itertools

#Calcular hash MD5
def calcularMD5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

#Calcular hash SHA-1
def calcularSHA1(texto):
    return hashlib.sha1(texto.encode()).hexdigest()

#Generar todas las combinaciones de 5 letras
def generarCombinaciones():
    abecedario = 'abcdefghijklmnopqrstuvwxyzñáéíóúü'
    return itertools.product(abecedario, repeat=5) #('s''o''l''a'r')

#Encontrar la contraseña y algoritmo utilizado
def encontrarPW(hashUsr):
    combinaciones = generarCombinaciones()
    
    for combinacion in combinaciones:
        password = ''.join(combinacion)
        # Calcular los hashes
        if len(hashUsr) == 32:
            hashMD5 = calcularMD5(password)
            if hashMD5 == hashUsr:
                return password, "MD5"
        else:
            hashSHA1 = calcularSHA1(password)
            if hashSHA1 == hashUsr:
                return password, "SHA-1"

    return None, None

def main():
    hashUsr = input("Ingresa un hash (MD5 o SHA1): ").strip()
    #Buscar la contraseña
    resultado, algoritmo = encontrarPW(hashUsr)

    if resultado:
        print(f"La contraseña encontrada es: {resultado}")
        print(f"El algoritmo de hash es: {algoritmo}")
    else:
        print("No se encontró ninguna contraseña que coincida con el hash proporcionado.")

if __name__ == "__main__":
    main()