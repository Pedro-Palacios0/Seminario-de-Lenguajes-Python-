def normalizar_registro(students):
    duplicados = {}
    copia_lista = students.copy()
    for alumno in copia_lista:
        if(alumno["name"] is None or alumno["name"].strip() == "" or
        alumno["grade"] is None or alumno["grade"].strip() == "" or
        alumno["grade"].strip().lower() == "absent"):
            students.remove(alumno)
        else:
            alumno["name"] = alumno["name"].strip().title()
            alumno["status"] = alumno["status"].strip().title()
            nombre = alumno["name"]
            if nombre not in duplicados:
                duplicados[nombre] = alumno
            else:
                if int(alumno["grade"]) > int(duplicados[nombre]["grade"]):
                    students.remove(duplicados[nombre])
                    duplicados[nombre] = alumno
                else:
                    students.remove(alumno)
    return sorted(students, key= lambda x: x["name"])