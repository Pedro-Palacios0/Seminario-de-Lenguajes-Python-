import random
def amigo_invisible(nombres):
    nombres = [nombre.strip().lower() for nombre in nombres]
    if len(nombres) >= 3 and len(nombres) == len(set(nombres)):
        copia_lista = nombres.copy()
        random.shuffle(copia_lista)
        while any(nombres[i] == copia_lista[i] for i in range(len(nombres))):
            random.shuffle(nombres)
        for i in range(len(nombres)):
            print(f"{nombres[i]} >> {copia_lista[i]}")
    else:
        print("Error.")