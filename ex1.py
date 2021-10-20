# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
# o valor unitário de cada peça 1, o código de uma peça 2, o número de peças
# 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3
# valores, respectivamente dois inteiros e um valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
# lembrando de deixar um espaço após os dois pontos e um espaço após o
# "R$". O valor deverá ser apresentado com 2 casas após o ponto.

linha1 = input().split()
linha2 = input().split()

linha1[0]
linha1[1]
linha1[2]

linha2[0]
linha2[1]
linha2[2]

cod1 = int(linha1[0])
quant1 = int(linha1[1])
var1 = float(linha1[2])

cod2 = int(linha2[0])
quant2 = int(linha2[1])
var2 = float(linha2[2])

result = (quant1 * var1) + (quant2 * var2)

print("VALOR A PAGAR: R$ {:.2f}".format(result))
