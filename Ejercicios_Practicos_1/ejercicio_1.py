otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio =  4
dalto_curso = 1.5

diferencia_entre_otros_cursos = 100 - ((dalto_curso / otros_cursos_min) * 100)
diferencia_entre_otros_lentos  = 100 - ((dalto_curso * 1000 // otros_cursos_max) / 10)
diferencia_entre_otros_promedio = 100 - ((dalto_curso / otros_cursos_promedio) * 100)
#print(diferencia_entre_otros_cursos)

print(f"el que estoy tomando es un {diferencia_entre_otros_cursos}% mas rapido que el mas rapido de los demas cursos")
print(f"el que estoy tomando es un {diferencia_entre_otros_lentos}% mas rapido que el mas lento de los demas cursos")
print(f"el que estoy tomando es un {diferencia_entre_otros_promedio}% mas rapido que el promedio de los demas cursos")


#Duracion de crudos {Variables}
crudo_promedio = 5
crudo_dalto = 3.5

tiempo_eliminado_de_los_crudos  = 100 - ((otros_cursos_promedio * 1000 // crudo_promedio) / 10)
dalto_tiempo_eliminado_de_los_crudos = 100 -((dalto_curso * 1000 // crudo_dalto)/10)
print(f"los otros cursos eleminan de sus crudos un {tiempo_eliminado_de_los_crudos}% de sus videos sin editar")
print(f"mientras que dalto de sus crudos elimina un {dalto_tiempo_eliminado_de_los_crudos} de sus videos sin editar")


#parte C del ejercicio 1.1py
print(f"ver 10 horas del curso de dalto equivale a ver {(otros_cursos_promedio * 100 // dalto_curso / 10)} de otros cursos")
print(f"ver 10 horas de otros equivale a ver {(dalto_curso * 100 // otros_cursos_promedio / 10)} del curso de dalto")


