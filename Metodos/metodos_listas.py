#creando una lista con list
lista = list(["Cesar", "Reynoso", 20])
#contando la cantidad de elementos con len
cantidad_elementos = len(lista)


print(lista[0], lista[1], lista[2])
print(cantidad_elementos)


#tanto con append como con insert se insertan elementos en la lista solo que insert ta da la opcion
#De decir en que indice quieres colocar ese elemento.
lista.append("Basket")
lista.insert(2, "CODING")

print(lista)
#Extend mas bien extiende la lista agregando mas de una elemento en un solo metodo para la lista.
lista.extend(["Jose",True])
lista.pop(2)
print(lista)

""" Como elimino un elemento de la lista el ultimo en especifico, viendo que la logica es el primero es el 0
pero el ultimo cual es, facil es el primero -1"""

lista.pop(-1)
print(lista)
"""Para aprender de remove pongamos el ejercicio a continuacion"""

lista.append("Basket")
print(lista)
lista.remove("Basket")
print(lista)
#Solo remueve una instacia de la busqueda no todas



lista2 = list([1,20,3,8,2,89,70])

lista2.reverse()
print(lista2)
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)
