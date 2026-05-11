def contar_lineas(text):
    return len(text.split("."))

def obtener_lineas(text):
    return text.splitlines()

def total_palabras(text):
    return len(text.split())

def promedio_palabras(text):
    return total_palabras(text) / contar_lineas(text)

def lineas_encima_promedio(text):
    for linea in obtener_lineas(text):
        palabras = len(linea.split())
        if palabras > promedio_palabras(text):
            print(f'  - "{linea}" ({palabras} palabras)')