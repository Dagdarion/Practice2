x = 1563847412

if (int(str(x)[::-1])) > (2 ** 31) - 1:
    print(0)
else:
    print(str(x)[::-1])
