
'''
Listas
* una lista es una secuencia de elementos.
* Cuando se asigna a una variable permite agrupar varios elementos 
 en un solo lugar.
* se crean con los [] o con la keyword list.
'''

lista1 = ["Roberto", 33, 9.5, True, "Cardiel", 20, 8]

print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Rodriguez")
print(lista1)

lista1.insert(2, "Laura")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(8)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["tres", "cuatro"]

lista3 = lista1 + lista2
print(lista3)

print(lista2*4)

lista4 = [2,1,5,4,3]
print(lista4)

lista4.sort()
print(lista4)

del lista4[0]
print(lista4)
