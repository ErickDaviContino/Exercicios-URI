cont = 0
end = True
media = 0

while end == True:
    nota = float(input())

    if nota >= 0.0 and nota <= 10.0:
        media += nota
        cont += 1

        if cont == 2:
            print("media = {:.2f}".format(media / 2))
            cont = 0
            media = 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                repetir = int(input())
                if repetir == 2:
                    end = False
                    break
                elif repetir == 1:
                    end = True
                    break

    else:
        print("nota invalida")
