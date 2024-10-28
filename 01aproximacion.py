

numero = int(input("dijita un numero: ") )
# aproximacion 
epsilon = 0.01
paso = epsilon**2
limite_inferior = 0.0




while abs(limite_inferior**2 - numero) >= epsilon and limite_inferior <= numero:
    limite_inferior += paso
    print(limite_inferior)
    
if abs(limite_inferior**2 - numero) >= epsilon:
    print(f"No encontramos la raiz cuadrada")
else:
    print(f"la raiz cuadrada de {numero} es {limite_inferior}")