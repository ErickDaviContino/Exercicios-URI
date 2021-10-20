import re

cont = int(input())

for i in range(cont):
    msg = input()
    msg_new = ''

    for l in msg:
        if re.match("[a-zA-Z]", l):
            msg_new += chr(ord(l) + 3)
        else:
            msg_new += l

    msg_new = msg_new[::-1]
    meio = int((len(msg_new) / 2))
    metad1 = msg_new[0:meio]
    metad2 = msg_new[meio:]
    metad_new = ''

    for l in metad2:
        metad_new += chr(ord(l)-1)

    texto_final = metad1+metad_new

    print(texto_final)
