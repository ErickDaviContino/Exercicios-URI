
while True:
    try:
        a, b, c = map(int, input().split())

        if (a == 1 or a == 0) and (b == 1 or b == 0) and (c == 1 or c == 0):
            if(a == b == c):
                print("*")
            elif(a == b):
                print("C")
            elif(a == c):
                print("B")
            else:
                print("A")
    except (EOFError):
        break
