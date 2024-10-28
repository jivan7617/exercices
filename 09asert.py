
#lista_palabras = [(input(" escribe el texto: "))]
lista_palabras = ["angulo",5.5,"", "   ", 542658, False]
def primer_letra(lista_palabras):
    primeras_letras = []
    
    
    
    for palabra in lista_palabras:
        
        try:
            assert type(palabra) == str, f" {palabra} no es un string"
            assert type(palabra) == 0, " no se permiten string vacios"
            primeras_letras.append(palabra[0])
            
        except AssertionError as error:
            print(error)
        
        
        
    return print(primeras_letras)

primer_letra(lista_palabras)
