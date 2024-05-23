age = int(input("Zadej věk:"))

if age >=65:
    print("Důchodce")
else:
    if age >= 18:
        print("plnoletý")
    else:
        if age >= 0:
            print("Nezletilý")
        else: 
            print("Neplatný věk")       