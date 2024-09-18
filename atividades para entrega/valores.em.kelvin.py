Kelvin = [275, 289, 292, 295, 297, 304, 311, 319, 324, 328]
Celsius = [round(x - 273.15,2) for x in Kelvin]
Fahrenheit = [round(x - 273.15,2) for x in Kelvin]
print ("{:<4}{:<8}{:<10}{:<6}".format("N°", "Kelvin", "Celsius", "Fahrenheit"))
print("|__|_______|________|_________")
for x in range(0,len(Kelvin),1):
    print("{:<4}{:<8}{:<10}{:<6}".format(x+1, Kelvin[x], Celsius[x], Fahrenheit[x]))