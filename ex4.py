quant = int(input())
print(quant)

quant100 = quant // 100
quant = quant - quant100 * 100

quant50 = quant // 50
quant = quant - quant50 * 50

quant20 = quant // 20
quant = quant - quant20 * 20

quant10 = quant // 10
quant = quant - quant10 * 10

quant5 = quant // 5
quant = quant - quant5 * 5

quant2 = quant // 2
quant = quant - quant2 * 2

quant1 = quant // 1
quant = quant - quant1 * 1

print('{} nota(s) de R$ 100,00'.format(quant100))
print('{} nota(s) de R$ 50,00'.format(quant50))
print('{} nota(s) de R$ 20,00'.format(quant20))
print('{} nota(s) de R$ 10,00'.format(quant10))
print('{} nota(s) de R$ 5,00'.format(quant5))
print('{} nota(s) de R$ 2,00'.format(quant2))
print('{} nota(s) de R$ 1,00'.format(quant1))
