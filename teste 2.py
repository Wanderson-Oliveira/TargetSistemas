import math

def check_fibonacci_number(n):
    # Verifica se a expressão é um quadrado perfeito
    return math.isqrt(5 * n * n + 4) ** 2 == 5 * n * n + 4 or math.isqrt(5 * n * n - 4) ** 2 == 5 * n * n - 4

# Solicita o número ao usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if check_fibonacci_number(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
