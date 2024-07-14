"""
Realiza una tupla llamada "tuplaPokemon" donde se encuentren los siguientes datos (respeta este orden):

pokemon
4
charmander
fuego
arañazo
llamarada
ascuas

"""
print("-------------------------------Tupla pokemon-------------------------------------------")
tuplaPokemon =("pokemon", 4, "charmander", "fuego", "arañazo","llamarada", "ascuas")
#una vez terminada la tupla, con esa tupla accede a los siguientes datos:

print(tuplaPokemon)# adentro de este print imprimir todos los valores de la tupla tuplaPokemon

print('\neste es un:') #acceder a la palabra 'pokemon' de la tupla tuplaPokemon
#tu respuesta con print:
print(tuplaPokemon[0])

print('\nsu nombre es:') #acceder a la palabra 'charmander' en tuplaPokemon
#tu respuesta con print:
print(tuplaPokemon[2])

print("\n y es de tipo:") #acceder a la palabra 'fuego' en tuplaPokemon
#tu respuesta con print:
print(tuplaPokemon[3])

print("\nsu numero en el poquedex es:") #acceder al '4' en tuplaPokemon
#tu respuesta con print:
print(tuplaPokemon[1])

print("\nsus ataques son:" ) #acceder a los elementos correspondientes a los ataques "arañazo", "llamarada", "ascuas" en tuplaPokemon
#tu respuesta con print:
print(tuplaPokemon[4:])

print("--------------------------------------------------------------------------")
print("\n\n" )

print("-------------------------------Tupla 2-------------------------------------------")
""" 
De la siguiente tuppla
"""

tupla2 = (4,4,3,"chihuahua","chihuahua","Mexico")

print(tupla2)

print("\nla cantidad de 4 son:") #obtener la cantidad de 4 en tupla2, usar metodo count
#tu respuesta con print:
print(tupla2.count(4))

print("\nla cantidad de palabra 'chihuahua' son:") #obtener la cantidad de "chihuahua" en tupla2, usar metodo count
#tu respuesta con print:
print(tupla2.count("chihuahua"))

print("\n la cantidad de la palabra 'enchilada' que encuentra en tupla2:") #usar metodo index con 'enchilada' en tupla2
#tu respuesta con print:
print(tupla2.count("enchilada"))


print("--------------------------------------------------------------------------")