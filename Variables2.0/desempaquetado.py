datos = {"Cesar", "Reynoso", 20}

nombre, apellido, edad = datos

print (edad, apellido, nombre)
print(datos)

tupla = tuple(["Cesar", "Reynoso","Jose","Martinez"])

print(tupla)

cadena = "Cesar"
contenedor = "Contenedor",

print(type(contenedor), type(cadena))


conjunto1 = frozenset(["Jeison Reyes", "Compañero", "CompuserviSuarez","Firt Job"])
conjunto2 = ([conjunto1, "Cesar R."] )

print(conjunto2)

numeros1 = {1,2,3,4,5,6,7,8,9,10,11,12}
numeros2 = {1,2,3,7}

resultado_conjuto_numeros = numeros2.issubset(numeros1)
resultado_conjuto_numeros2 = numeros2.isdisjoint(numeros1)

print(resultado_conjuto_numeros)
print(resultado_conjuto_numeros2)
