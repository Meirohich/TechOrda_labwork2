a = int(input())
for n in range(2, a+1):
    if a % n == 0:
        print(n)
        break
