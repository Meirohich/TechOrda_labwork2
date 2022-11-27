def Election(x, y, z):
    if x + y + z == 0:
        print(0)
    elif (x == 1 and y == 1) or (x == 1 and z == 1) or (y == 1 and z == 1):
        print(1)
    else:
        print(0)


x, y, z = [int(x) for x in input().split()]
Election(x,y,z)