import random

diccionario = {
    "programacion" : ["python", "programa", "lista", "variable", "funcion"],
    "animales" : ["gato", "perro", "cebra", "leon"],
    "materias" : ["fod", "ayed", "seminario", "matematica"]}

print("¡Bienvenido al Ahorcado!")
print()
print("Categorias disponibles")
for categorias in diccionario:
    print(f"- {categorias}", end="")
print()
eligio = False
while not eligio:
    cat_elegida = input("Eliga una categoria: ").lower()
    if cat_elegida in diccionario:  
        words = diccionario[cat_elegida]
        lista= random.sample(words, len(words))
        eligio = True
    else:
        print("Categoria no valida, vuelva a elegir.")

puntaje_total = 0
for word in lista:
    print("Arranca la ronda!!!")
    guessed = []
    attempts = 6
    gano = False
    puntaje_ronda = 0
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            gano = True
            puntaje_ronda += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        
        letter = input("Ingresá una letra: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no valida.")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje_ronda -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje_ronda = 0
    puntaje_total += puntaje_ronda
    print(f"Tu puntaje en la ronda fue: {puntaje_ronda}" )
print(f"Tu puntaje total fue de: {puntaje_total}")