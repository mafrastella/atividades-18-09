Quilos = [4,7,18,20,26,33,41,47,52,60]
Terra = [round(x * 9.81 ,2) for x in Quilos]
Lua = [round(x * 1.6 ,2) for x in Quilos]
Marte = [round(x * 3.8 ,2) for x in Quilos]
Mercúrio = [round(x * 0.38 ,2) for x in Quilos]
print ("{:<4} {:<8} {:<10} {:<6} {:<8} {:<8}".format("N°", "Quilos", "Terra", "Lua", "Marte", "Mercúrio"))
print("|__|_______|__________|_______|________|_________")
for x in range(0,len(Quilos),1):
    print("{:<4}{:<8}{:<12}{:<8}{:<10}{:<8}".format(x+1, Quilos[x], Terra[x], Lua[x], Marte[x], Mercúrio[x]))