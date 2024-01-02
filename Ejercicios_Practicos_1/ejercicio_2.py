frase  = input("ingresa una frase: ")
fragments  = frase.split(" ")
cantidad_de_palabras =  len(fragments)
print(f"Digiste {cantidad_de_palabras} palabras por lo que tardarias alrededor de\n{cantidad_de_palabras/2}s\nSegundos en decirlo")