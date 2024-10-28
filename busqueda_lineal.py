import random

def busqueda_lineal(lista, busqueda):
    match = False
    
    for elemento in lista:  #complejidad O(n)
        if elemento == busqueda:
            match = True
            break
        
    return match

tamaño_de_lista= int(input("dijita el tamaño de la lista "))
busqueda = int(input("que numero quieres encontrar? "))
    
lista = [random.randint(0,100) for i in range(tamaño_de_lista)]


if __name__ == "__main__":
   
    encontrado = busqueda_lineal(lista, busqueda)
    
    print(lista)
    print(f'el elemento {busqueda} {"esta" if encontrado else "no esta"} en la lista ')  