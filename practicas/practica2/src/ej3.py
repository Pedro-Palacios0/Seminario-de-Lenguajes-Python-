def reemplazar_palabras(lista,review):
    lista = [palabra.strip().lower() for palabra in lista]
    lista_review = review.split()
    resultado = []
    for palabra in lista_review:
        if palabra.lower() in lista:
            resultado.append("*" * len(palabra))
        else:
            resultado.append(palabra)
    return " ".join(resultado)