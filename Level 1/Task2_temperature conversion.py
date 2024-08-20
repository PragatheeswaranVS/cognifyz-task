def fahrenheit_to_Celsius(celsius):
    return (celsius * 1.8) + 32
def Celsius_to_fahrenheit(fahrenheit):
    return (fahrenheit-32)/1.8
temperature = float(input("Enter the temperature : "))
unit = input("Enter F to convert fahrenheit\tor\tEnter C to convert Celsius :")
unit = unit.upper()
if unit == "F":
    f= Celsius_to_fahrenheit(temperature)
    print(f" The conversion of fahrenheit to celsius is {f:.2f} Celsius")
elif unit == "C":
    c= fahrenheit_to_Celsius(temperature)
    print(f" The conversion of celsius to fahrenheit is {c:.2f} fahrenheit")


'''
OUTPUT:-

Enter the temperature : 30
Enter F to convert fahrenheit   or      Enter C to convert Celsius :c
 The conversion of celsius to fahrenheit is 86.00 fahrenheit
 
Enter the temperature : 86
Enter F to convert fahrenheit   or      Enter C to convert Celsius :f
 The conversion of fahrenheit to celsius is 30.00 Celsius
'''