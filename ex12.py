abc = input().split()
abc = list(map(float, abc))

a, b, c = sorted(abc)[::-1]

segue = True

if(a >= b+c):
    print("NAO FORMA TRIANGULO")
    segue = False

if(a ** 2 == (b ** 2) + (c ** 2) and segue):
    print("TRIANGULO RETANGULO")

if(a ** 2 > (b ** 2) + (c ** 2) and segue):
    print("TRIANGULO OBTUSANGULO")

if(a**2 < (b ** 2) + (c ** 2) and segue):
    print("TRIANGULO ACUTANGULO")

if(a == b and b == c and segue):
    print("TRIANGULO EQUILATERO")

if((a == b or b == c) and not (a == b and b == c) and segue):
    print("TRIANGULO ISOSCELES")
