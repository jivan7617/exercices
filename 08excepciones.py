

lista = range(1,21)

divisor = int(input("digita un numero: "))
def dividir_elementos(lista, divisor):
    try:
        return[i/ divisor for i in lista]
    
    except ZeroDivisionError as error:
        print(error)
        
        
print(dividir_elementos(lista,divisor))

