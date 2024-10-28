

contador_interno= 0
contador_externo= 0

while contador_externo < 5:
    while contador_interno< 6:
        print(f"externo = {contador_externo}", f"interno = {contador_interno}")
        contador_interno+=1
        # el contador se interumpe en 2
        if contador_interno >=3:
            break
        
    contador_externo +=1
    contador_interno = 0
"""   Podemos modificar el comportamiento de un bucle for mediante los keywords
break y continue pass .

break termina el bucle y permite continuar con el resto del flujo de nuestro
programa.

pass = no hay nada mas

continue termina la iteración en curso y continua con el siguiente ciclo de
iteración. """
    