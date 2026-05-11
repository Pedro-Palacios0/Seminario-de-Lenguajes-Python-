def validar_email(email):
    partes = email.split("@")
    partes_punto = email.split(".")
    if (email.count("@") == 1 and 
        partes[0] != "" and
        partes[1].count(".") == 1 and
        not email.startswith("@") and
        not email.endswith(".") and
        len(partes_punto[-1]) >= 2):
        print("Valido")
    else:
        print("Invalido")