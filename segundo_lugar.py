#Dada la hoja de puntuación de los participantes para su Día del Deporte Universitario, deberá encontrar la puntuación del segundo lugar. Te dan puntuaciones. Guárdelos en una lista y encuentre la puntuación del subcampeón.

#La primera línea contiene n . La segunda línea contiene una matriz de A [ ] números enteros, cada uno separado por un espacio.
#2<= n <=10
#-100<= A[i]<=100


num = 1

arr = [8,6,9,9,7,9]
list_order = sorted(arr)  
list_separate = ' '.join(map(str,arr))   
posicion = len(list_order)-1
anteriori = posicion - num

if 2 <= num <= 10 and all(-100 <= x <= 100 for x in arr):
    while list_order[posicion] == list_order[anteriori]:
        num += 1
        anteriori = posicion - num
    else:
        print (list_order[anteriori])
        print(list_separate)




    
    
