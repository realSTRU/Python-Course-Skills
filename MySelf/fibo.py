def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n - 2)
    
n = input("Digite la cantidad de numeros de fibo que desea generar:")

numero = int(n)
for i in range(numero):
    print(f"numero {i}:{fibo(i)}\n")