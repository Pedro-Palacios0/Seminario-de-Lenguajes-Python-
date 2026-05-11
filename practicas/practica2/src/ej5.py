precios = {
    "local" : [500,1000,2000],
    "regional" : [1000,2500,4500],
    "nacional" : [2000,4500,8000]
}
def calculo_costo(peso,zona):
    if zona in ("local", "regional","nacional"):
        if peso <= 1:
            indice = 0
        elif peso <= 5:
            indice = 1
        else:
            indice = 2
        return precios[zona][indice]
    else:
        return "Zona invalida."