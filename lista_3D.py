# Se le dan tres números enteros x, y, z que representan las dimensiones de un cuboide junto con un número entero n. Imprima una lista de todas las coordenadas posibles dadas por (i, j, k) en una cuadrícula 3D donde la suma de (i + j + k) no es igual a n. Aquí, (0<= i <= x; 0 <= j <= y; 0 <= k <= z). Utilice listas de comprensión en lugar de bucles múltiples

x = 1
y = 1
z = 2
n = 3

#lista_comprension = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]


cuadricula_4D = [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

cuadricula_3D = [[i, j, k] for i in range(0, (x + 1)) for j in range(0, (y + 1)) for k in range(0, (z + 1)) if (i + j + k) != n]

print(cuadricula_4D)
print(list(cuadricula_3D))