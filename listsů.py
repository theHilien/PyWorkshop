#Vytvoření seznamu

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
seznam_str = ["jahoda", "banán", "dort", "okurka", "jablko" ]

print (seznam)
print (seznam_str[2])
print (seznam_str[-1])
print ("Délka:", str(len(seznam_str)))

seznam_str.append("koláč")
seznam.append(0)

print (seznam)
print (seznam_str)
print (seznam_str[-1])
print ("Délka:", str(len(seznam_str)))

seznam.sort(reverse=True)
print(seznam)
seznam_str.sort(reverse=True)
print(seznam_str)

seznam_str[-1] = ("skořice")
seznam[-1] = 11
print(seznam)
print(seznam_str)

del seznam[1]
del seznam_str[1]
print(seznam)
print(seznam_str)

seznam.insert(1,"koláč")
print(seznam)

