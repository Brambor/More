import msvcrt

a = 0
while True:
    char = msvcrt.getch()
    print(char)
    if (char == b'a'):
        a -= 1
    elif (char == b'd'):
        a += 1
    print(a)
