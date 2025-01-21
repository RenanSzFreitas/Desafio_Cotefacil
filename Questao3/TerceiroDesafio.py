import sys

# Função para calcular o n-ésimo número da sequência de Fibonacci (recursiva)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Aqui ele verifica se o número é válido
if len(sys.argv) != 2:
    print("Por favor, forneça um número inteiro positivo:")
    sys.exit(1)

# Ele obtém o número 'n'
n = int(sys.argv[1])

# Verifica se o número é positivo
if n < 0:
    print("O número deve ser inteiro positivo!")
    sys.exit(1)

# Calcula e imprime o n-ésimo valor da sequência de Fibonacci
print(fibonacci(n))