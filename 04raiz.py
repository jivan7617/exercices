numero = int(input("dijita un numero: "))
raiz = 0

while raiz **2 < numero:
    raiz +=1
    print(raiz)
    
if raiz **2 == numero:
    print(f"la raiz cuadrada de {numero} es {raiz}")
else:
    print(" el numero {numero} no tiene raiz cuadrada")    