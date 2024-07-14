#######################################################

#        1er 2do 3er 4to 5to 6to 7mo 8vo 9no  10mo   <<Elemento de la lista
#        0   1   2   3   4   5   6   7   8    9      <<indice del arreglo
lista = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10]

print("\nLista sencilla:\n")
print (lista)
print("\n-------------------------------------------------------------\n")

#######################################################

#          Tiene 11 caracteres
#         012345678910                 <<indice del arreglo
nombre = "Super Bowl"
print (nombre)
print("\nDe string(cadena de caracteres) a lista:\n")
lista = list(nombre)

print (lista)
print("\n-------------------------------------------------------------\n")
#######################################################


tupla = (1,  3,  "Perro", "México", True, "3.29")
print (tupla)
print("\nDe tupla a lista:\n")
# Recuerda que tambien se puede viceversa

lista = list(tupla)

print(lista)
print("\n-------------------------------------------------------------\n")
#######################################################


#            1er      2do       3er         4to       <<Elemento de la lista
#            0        1         2           3         <<indice del arreglo
lista = ["Alfonso","Rocio","Carolooos", "Fulanito"]

print(lista)
print("\nAgregar elemento al último lugar de una lista (agregar 3 int):\n")

#Aquí se agrega un elemento extra al final de la lista con METODO .append()
lista.append(3)

print(lista)
#-------------------------------------------------------
print("\nAgregar una TUPLA al último lugar de una lista:\n")
#agregar una tupla al final de la lista

tupla = (1, True, "Hola")

print(tupla)

lista.append(tupla)

print(lista)

#-------------------------------------------------------

print("\nSe puede cambiar un valor a un elemento de una lista (cambiar 'Carolooos' por 'Carlos'):\n")

lista[2]="Carlos"

print(lista)

#-------------------------------------------------------

print("\nSe puede cambiar un valor a un elemento de una lista (cambiar 'Alfonso' por valor entero de 439 ):\n")

lista[0] = 439

print(lista)
print("\n-------------------------------------------------------------\n")
#######################################################
#agregar un elemento en cualquier parte de la lista


#        1er 2do 3er 4to 5to 6to 7mo   <<Elemento de la lista
#        0   1   2   3   4   5   6     <<indice del arreglo
lista = [1,  2,  3,  4,  5,  6,  7]
print(lista)

print("\n se agrega un elemento, se agrega la cadena de caracteres 'Elemento Cualquiera' a segundo elemento (indice 1) de la lista: ")

elemento_cualquiera = "Elemento Cualquiera"

lista.insert(1, elemento_cualquiera)

print(lista)


print("\n-------------------------------------------------------------\n")
#######################################################
# eliminar el ultimo elemento

#           1er    2do   3er     4to  5to 6to 7mo 8vo   <<Elemento de la lista
#            0      1     2       3    4   5   6   7    <<indice del arreglo
lista = [(3.23,45), 34, "Hola", False, 4,  3,  4,  4]
print(lista)

print("\nsi no se pone nada dentro de los parentecis de .pop() se borra el ultimo elemento (tambien se puede poner .pop(-1) ): ")
lista.pop()

print(lista)


print("\nse coloca el indice del elemento que se quiere eliminar por ejemplo el 3er elemento ('Hola') con .pop(2):")
#           1er    2do   3er     4to  5to 6to 7mo 8vo   <<Elemento de la lista
#            0      1     2       3    4   5   6   7    <<indice del arreglo
lista = [(3.23,45), 34, "Hola", False, 4,  3,  4,  4]

lista.pop(2)
print(lista)

print("\n-------------------------------------------------------------\n")

##########################################################
#       1er           2do          3er    4to      5to                            6to                                  <<Elemento de la lista
#        0             1            2      3        4                             5                                    <<indice del arreglo
lista = [1,  ("tupla",True,23.5),  235,  "Hola",  234.23, {'clave1': 'valor1','clave2': 'valor2','clave3': 'valor3'}]

print(lista)

print("la longitud de esta lista es:")
longitud_de_lista = len(lista)
print(longitud_de_lista)

