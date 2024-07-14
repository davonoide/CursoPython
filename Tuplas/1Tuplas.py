#TUPLAS
#posicion de elementos:
#      1er 2do     3er         4to           5to      6to 7mo
#posicion de indices:
#      0   1       2           3             4        5   6
tupla=(4,"hola", 7.18, [11,23,100,"perro"],"ALIENS",  4,  4)
#NOTA: la lista [11,23,100,"perro"] es el 4to elemento y a su vez tiene indice 3

print(f"nuestra tupla contiene: {tupla}")

####### LO QUE NO SE PUEDE HACER####
#
#en una tupla NO se pude usar el metodo de .append()
#tupla.append()
#la tupla NO puedes modificar los valores
#tupla[0]=8
#en una tupla NO puedes eliminar valores
#tupla.pop()
#
####################################



##### lo que SI SE PUEDE #######

#se pueden mostrar los elementos
print("se puede mostrar el primer elemento:")
print(tupla[0])
print("------------------------------------------------------------")

print(f"se puede mostrar cuarto elemento: \n{tupla[3]}")

print("------------------------------------------------------------")

print(f"se puede mostrar el segundo elemento de la lista hasta el que está en el cuarto elemento de la tupla: \n{tupla[3][1]}")

print("------------------------------------------------------------")

print(f'si se quiere acceder al elemento "perro" que está en la lista dentro de la tupla se pone tupla[3][3]: \n{tupla[3][3]}')

print("------------------------------------------------------------")

print(f'se puede acceder a del segundo elemento en adelante con tupla[1:]: \n{tupla[1:]}')
print(f"se puede seleccionar una seccion de la tupla por ejemplo del elemento 2 al 4: {tupla[1:4]}")

print("------------------------------------------------------------")

print(f"comprobar si el valor de 7.18 esta dentro de la tupla: {7.18 in tupla}")

print("------------------------------------------------------------")

print(f"comprobar si el valor de 'ALIENS' esta dentro de la tupla: {"ALIENS" in tupla}")
print(f"comprobar si el valor de 'aliens' esta dentro de la tupla: {"aliens" in tupla}")

print("------------------------------------------------------------")

print(f"se puede usar el metodo index para encontrar la posicion del elemento dentro de tupla por ejemplo con 'hola': {tupla.index('hola')}")
print(f"se puede usar el metodo index para encontrar la posicion del elemento dentro de tupla por ejemplo con 'ALIENS': {tupla.index('ALIENS')}")

print("------------------------------------------------------------")

print("se puede contar cuantos elementos iguales hay en la tupla, por ejemplo el 4:")
contar4EnTupla= tupla.count(4)
print(contar4EnTupla)

print(f"se puede contar cuantos elementos iguales hay en la tupla, por ejemplo 'ALIENS': {tupla.count("ALIENS")}")

print("------------------------------------------------------------")
print(f"se puede saber cuantos elementos hay en las tuplas: {len(tupla)}")
print("------------------------------------------------------------")

print("se puede convertir una tupla a lista:")
lista= list(tupla)
print(lista)

print("\n")
print("se puede cambiar un valor en una lista por ejemplo lista[0]=1:")
lista[0]=1
print(lista)
print("\n")

print("------------------------------------------------------------")
print("una lista se puede transformar a una tupla:")

tupla2=tuple(lista)
print(tupla2)




