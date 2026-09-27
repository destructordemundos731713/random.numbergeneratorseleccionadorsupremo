import random

lista = []
datos_filtrados = [] 

for i in range(10):
    
    numero_al_azar = random.randint(1, 20) 
    lista.append(numero_al_azar)


for numero in lista: 
    if numero > 10:
        datos_filtrados.append(numero)
    else:
        pass 


print("Datos originales:", lista)
print("Datos mayores a 10:", datos_filtrados)
