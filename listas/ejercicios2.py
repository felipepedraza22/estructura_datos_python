# Ejercicios Listas

#Metodos propios

lista=[45, 32, 3, 78]
print("Lista original:", lista)
# Funcion append: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista despues de usar append ", lista)
#Funcion sert: ordena la lista
lista.sort()
print("Lista ordenada:", lista)
# Funcion reverse: Invierte el orden de la lista
lista.reverse()
print("Lista al reves:", lista)
#Funcion extend:  añade los elementos de una lista a la lista 
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend:", lista)
# Funcion count: Cuenta el numero de veces que aparece el elemento indicado conparametro dentro de la lista
print("Numero de elementos 45:", lista.count(45))
# Funcion insert: añade ek elemento pasado como parametro a la lista en la posicion indicada tambien por parametro
lista.insert(4,111)
print("Lista despues de insert:", lista)
# Funcion remove: Elimina la primera ocurencia empezando por la izquierda de la lista del elemento indicado como parametro
lista.remove(45)
print("Lista despues de remove:", lista)
# Funcion index:devuelve la posicion de la primera ocurencia de izquierda a derecha de la lista, del elemento pasado como parametro
print("Posicion del elemento 111", lista.index(111))
# Funcion pop: Elimina un elemento de la lista y lo devuelve como rexsultado de la operacion
lista.pop()
print("Lista despues de pop:", lista)
# Funcion clear: Elimina todos los elementos de la lista
lista.clear()
print("Lista despues de clear:", lista)