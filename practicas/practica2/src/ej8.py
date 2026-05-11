def cifrar(mensaje, desplazamiento):
    resultado = ""
    for letra in mensaje:
        if letra.islower():
            resultado += chr((ord(letra) - ord("a") + desplazamiento) % 26 + ord("a"))
        elif letra.isupper():
            resultado += chr((ord(letra) - ord("A") + desplazamiento) % 26 + ord("A"))
        else:
            resultado += letra
    return resultado