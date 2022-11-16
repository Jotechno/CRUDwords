#Ingresar cuantas palabras y que palabra agregar / How many words and whaat word add to the list
def ingresarPalabras():
    i = 0
    cantidadPalabras = int(input("\nIngrese cuantas palabras quiere añadir: "))
    while i < cantidadPalabras:
        palabra = input("Ingrese la palabra: ")
        lista.append(palabra)
        i += 1

#Mostrar cuantas palabras haay / Show how many words are in the list
def cantidadPalabras():
    print(f"\nLa lista tiene un total de {len(lista)} elementos.")

#Sustituir una palabra con otra  / Substitute a word for another 
def sustiturPalabra():
    indice = int(input("\nIngrese la posición donde quiere sustituir la palabra: "))
    palabra = input("Ingrese la palabra sustituta: ")
    lista[indice] = palabra

#Borrar una palabra / delete a word
def eliminarPalabra():
    palabra = input("\n¿Qué palabra desea remover?\n ")
    lista.remove(palabra)

#ordenar lista alfabeticamente / sort list alphabetically
def ordenarLista():
    lista.sort()
    print("\nLa lista ha sido ordenada.")

#Muestra el tipo y la longitud de la lista / show the type and the length of the list
def tipoLongitud():
    print(f"\nLa lista es tipo {type(lista[0])} y tiene un total de {len(lista)} elementos.")

#Mostrar la lista / show the list 
def mostrarLista():
    for i in range(0, len(lista)):
        print(i, lista[i])

#Crear la lista y mostrar las opciones del menu / Create the list and shows the menu options
lista = []
opcion = int(input("Menú Principal\nOpción 1: Ingresar N palabras a la Lista.\nOpción 2: Contar el número de palabras que tiene la lista.\
    \nOpción 3: Sustituir una palabra en una posición específica de la lista.\nOpción 4: Eliminar una palabra de la lista.\
    \nOpción 5: Ordenar la lista de palabras. \nOpción 6: Mostrar el tipo y longitud de la lista\nOpción 7: Mostrar la lista.\
    \nOpción 8: Salir de la aplicación\n\nIngrese su opción: "))

#Bucle que se repetirá hasta que se elija la opción 8 / The loop will continue until the user choose the option 8
while True:
    

    if opcion == 1:
        ingresarPalabras()
    elif opcion == 2:
        cantidadPalabras()
    elif opcion == 3:
        sustiturPalabra()
    elif opcion == 4:
        eliminarPalabra()
    elif opcion == 5:
        ordenarLista()
    elif opcion == 6:
        tipoLongitud()
    elif opcion == 7:
        mostrarLista()
    elif opcion == 8:
        print("\nHasta luego")
        break
    opcion = int(input("\nIngrese otra opción: "))