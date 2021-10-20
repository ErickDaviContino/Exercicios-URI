valorPago = 1
valorProduto = 1

while valorPago != 0 and valorProduto != 0:
    valorPago, valorProduto = map(int, input().split())

    if valorPago == 0 or valorProduto == 0:
        break
    else:
        troco = valorProduto - valorPago

        if (troco == 7 or troco == 12 or troco == 22 or troco == 52 or troco == 102 or troco == 15 or troco == 25 or troco == 55 or troco == 105 or troco == 30 or troco == 60 or troco == 110 or troco == 70 or troco == 120 or troco == 150):
            print("possible")
        else:
            print("impossible")
