def duracion_total(playlist):
    minutos_totales = 0
    segundos_totales = 0
    for cancion in playlist:
        tiempo = cancion["duration"]
        div = tiempo.split(":")
        minutos_totales += int(div[0])
        segundos_totales += int(div[1])
    minutos_totales += segundos_totales // 60
    segundos_totales = segundos_totales % 60
    return minutos_totales, segundos_totales

def cancion_mas_y_menos_larga(playlist):
    tiempo_cancion_maslarga = -1
    tiempo_cancion_mascorta = 100000
    cancion_maslarga = None
    cancion_mascorta = None
    for cancion in playlist:
        div = cancion["duration"].split(":")
        total = int(div[0]) * 60 + int(div[1])
        if total > tiempo_cancion_maslarga:
            cancion_maslarga = cancion
            tiempo_cancion_maslarga = total
        if total < tiempo_cancion_mascorta:
            cancion_mascorta = cancion
            tiempo_cancion_mascorta = total
    return cancion_maslarga, cancion_mascorta
