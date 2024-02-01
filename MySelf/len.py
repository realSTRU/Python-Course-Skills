nombre = input("Digita tu nombre: ")
name_fragments = nombre.split(" ")
print(f"{name_fragments}, {len(name_fragments)}")

noun_count = len(name_fragments)

print(f"Tu nombre almacenado es {name_fragments}\nTu nombre completo tiene la cantidad de: {noun_count} sustantivos")

