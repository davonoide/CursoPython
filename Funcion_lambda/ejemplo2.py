"""
estructura de funcion lamda:

lambda {aqui todas las variables} : {funcion}

"""



lista_estudiantes = [
                    ("Raul",9.34),
                    ("Laura",8.7),
                    ("Ramiro",10),
                    ("Federico",7.9),
                    ("Maria",8.4),
                    ("Carlos",9.34),
                    ("Luis",5.9),
]

"""def por_nombre(tupla):
    return tupla[0]

def por_calificacion(tupla):
    return tupla[1]"""

#lista_ordenada = sorted(lista_estudiantes, key= por_nombre, reverse=False)

#lista_ordenada = sorted(lista_estudiantes, key= por_calificacion, reverse=False)


lista_ordenada = sorted(lista_estudiantes, key= lambda x:x[1], reverse=False)

#lista_ordenada = sorted(lista_estudiantes, key= lambda x:x[0], reverse=False)


print(lista_ordenada)

##### imprimiendo lo que esta obteniendo 

for alumno_info in lista_estudiantes:

    print(alumno_info)

for alumno_info in lista_estudiantes:
    nombre = lambda x : x[0]
    #nombre = lambda tupla : tupla[0]
    print(nombre(alumno_info))

voltear = "987654321"

print(voltear[4:7:])