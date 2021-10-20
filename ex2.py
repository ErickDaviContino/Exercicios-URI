# Faça um programa que leia três valores e apresente o maior dos três valores
# lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

# obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
# Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

var = input().split()

var[0]
var[1]
var[2]

a = int(var[0])
b = int(var[1])
c = int(var[2])

form = (a + b + abs(a - b)) / 2

if form > c:
    print("{:.0f} eh o maior".format(form))
else:
    print("{:.0f} eh o maior".format(c))
