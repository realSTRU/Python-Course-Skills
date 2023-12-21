#Ojo utiliza snake_case for python

a = 2023
b = 2003
c = a - b
nombre = "Cesar"


print(f"Hola soy {nombre} y tengo {c} años")
print(c)

numero = 10
numero += 3
numero += 7

print(numero)

#concatenando con fstrings
enunciado = f"Hola soy {nombre} y tengo {c} años"
print(enunciado)

#concatenando con el +
enunciado_obsoleto = "Cesar" + " Es un mal programador"
print(enunciado_obsoleto)

#Cuanto utilizamos la palabra del antes de la definicion de una variable en la misma linea como
# del numero la variable no estaria definida para el punto en que se borro con la palabra reservada del
# in y not in son mas funciones de las cuales devuelven un valor boolean en conforme a pertenencias de texto#

valor = "Hola" in enunciado
valor_2 = "Hola" not in enunciado
print (valor_2, valor)

#Output del archivo
#Hola soy Cesar y tengo 20 años
#20
#20
#Hola soy Cesar y tengo 20 años
#Cesar Es un mal programador
#False True 
""" 
yo prefiero usar esto en verdad para hacer comentarios 
Hola soy Cesar y tengo 20 años
20
20
Hola soy Cesar y tengo 20 años
Cesar Es un mal programador
False True
"""
