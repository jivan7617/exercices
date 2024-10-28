
# busqueda binaria (solo si los numeros estan ordenados )
#aproximasion de un numero

# aproximacion 
numero = int(input("dijita un numero: ") )
epsilon = 0.001
paso = epsilon**2
limite_inferior = 0.01
limite_superior = max(1, numero)
respuesta= (limite_inferior + limite_superior) /2

while abs(respuesta**2 - numero) >= epsilon:
    print(f"inferior {limite_inferior} superior {limite_superior} respuesta {respuesta} ")
    if respuesta**2 < numero:
        limite_inferior = respuesta
        
    else:
        limite_superior = respuesta
        
    respuesta = (limite_inferior + limite_superior)/2
    
    print (f"la raiz cuadrada de {numero} es {respuesta}")