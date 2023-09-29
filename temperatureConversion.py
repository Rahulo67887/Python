temp=float(input("Enter the temperature:"))
unit=input("What is the unit of this temperature(C/F):")

if unit=="C" or unit=="c":
    temp=round((9*temp)/5+32,1)
    print(f"The temperature in fahrenheit is {temp}F")
elif unit=="F" or unit=="f":
    temp=round((temp-32)*5/9,1)
    print(f"The temperature in celsius is {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")