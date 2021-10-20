'''
Escreva um algoritmo que leia dois valores flutuantes (x e y), 
que devem representar as coordenadas de um ponto em um plano. Em 
seguida, determine a qual quadrante o ponto pertence ou se você está 
em um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem "Origem".

Se o ponto está no eixo X escreva "Eixo X", senão se o ponto está no eixo Y escreva "Eixo Y".

Entrada
A entrada contém as coordenadas de um ponto.

Saída
A saída deve exibir o quadrante em que o ponto está.
'''
cordenada = input().split()

cordenada[0]
cordenada[1]

x = float(cordenada[0])
y = float(cordenada[1])

if x == 0:
    if y == 0:
        print('Origem')
    if y != 0:
        print('Eixo Y')
if y == 0:
    if x != 0:
        print('Eixo X')
if x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
if x < 0:
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')
