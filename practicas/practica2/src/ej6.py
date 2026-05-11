from collections import Counter
def frecuencia_hashtags(texto):
    hashtags = []
    for renglon in texto:
        for palabra in renglon.split():
            if palabra.startswith("#"):
                hashtags.append(palabra)
    return Counter(hashtags)

