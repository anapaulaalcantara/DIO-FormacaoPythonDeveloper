T = int(input())

for i in range(T):
    ''' 
    TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
         para obtenção dos valores.
    TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
         aproveitar ao máximo a oferta.
    ''' 
  
    N, K = map(int, input().split())
    GARRAFAS = N//K + N%K
    print(GARRAFAS)