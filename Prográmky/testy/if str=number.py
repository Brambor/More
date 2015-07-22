while True:
    a=input()
    if a.isdigit():
        print("It is number.")
    elif a=="exit":
        break
    else:
        print("It isn't number.")
