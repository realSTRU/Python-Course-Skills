nombre = "Cesar Jose Reynoso Martinez"
cedula ="056-7892340-9"

print(dir(nombre)) 
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())
print(nombre.find("Jose"))
print(nombre.find("Martinez"))
print(cedula.index("7"))


numero = cedula.count("0")
value_of_numero_two = len(cedula)

print (numero, value_of_numero_two)
new_cedula = cedula.replace("056", "402")

print(new_cedula, cedula)
fragments = cedula.split("-")
print(fragments[0], fragments[1], fragments[2])

