Metros = [4,7,18,20,26,33,41,47,52,60]
Polegadas = [round(x * 39.37,2) for x in Metros]
Pés = [round(x * 3.281,2) for x in Metros]
Jardas = [round(x * 1.094,2) for x in Metros]
Milhas = [round(x / 1852,2) for x in Metros]
print ("{:<4} {:<6} {:<12} {:<8} {:<8} {:<8}".format("N°", "Metros", "Polegadas", "Pés", "Jardas", "Milhas"))
print("|__|_______|__________|_______|________|_______")
for x in range(0,len(Metros),1):
    print("{:<6}{:<6}{:<12}{:<8}{:<8}{:<8}".format(x+1, Metros[x], Polegadas[x], Pés[x], Jardas[x], Milhas[x]))