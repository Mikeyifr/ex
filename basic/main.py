deg = float(input("enter the degree (c/f): "))
scale = input("enter the scale: ")
if scale == "c" or scale == "C":
    print((deg * 1.8) + 32)
elif scale == "f" or scale == "F":
    print((deg - 32) / 1.8)
else:
    print("invalid choise")