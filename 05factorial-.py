

n = int (input( "dijita un numero :" ))

def factorial(n):
    """
    Args:
        int n > 0 : retorna n! (factorial)
    """
    print(f"{n} * ")
    if n == 1:
        return 1 
     
    return (n * factorial (n - 1))


print( f" = {factorial(n)}")