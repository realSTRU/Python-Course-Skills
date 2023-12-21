list = ["Cesar", "Reynoso", 
        "20", "5,11", "Basketball", "Shooters"]
tuple = ("Cesar", "Reynoso", 
        "20", "5,11", "Basketball", "Shooters")
#The tuples can´t modified while list can do it
print(f"mi nombre es {list[0]} {list[1]} tengo {list[2]} y mido unos {list[3]} me gusta jugar {list[4]} y amo los {list[5]}")


set= {"Cesar", "Reynoso", 
        "20", "5,11", "Basketball", "Shooters"}

#los set no se pueden modificar al menos en la composicion de los elementos individuales
#pero si se puede reconstruir -Reestructurar- no son accedibles por indices y los elementos no se pueden repetir en caso de los strings 
print(set)

#Diccionarios
diccionarios = {
    'nombre' : "Cesar",
    'apellido' : "Reynoso",
    'edad' : 20,
    'Hobby' : "Programacion web"
}


print(diccionarios['Hobby'])