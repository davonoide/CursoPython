""" def suma(x,y):
    return(x+y)  """

suma = lambda x,y: x+y


print(suma(5,4))
print(suma(10.453,4.2))
#print("{:.3f}".format(suma(10.453,4.2)))
"""
total = suma(10.453,4.2)
formateado = f"{total:.3f}"

print(formateado)
print(type(formateado))
"""

lista = [1,2,3,4,5,6,7,8,9,10]
listadoble = []

for numero in lista:
    doble = lambda num :num*2
    listadoble.append(doble(numero))

print(listadoble)