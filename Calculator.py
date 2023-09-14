num1=float(input("Enter first num:"))
num2=float(input("Enter second num:"))
operator=input("Enter an operator(+ - / *):")

if operator=="+":
    result=num1+num2
    print(round(result,3))
elif operator=="-":
    result=num1-num2
    print(round(result,3))
elif operator=="*":
    result=num1*num2
    print(round(result,3))
elif operator=="/":
    result=num1/num2
    print(round(result,3))
else:
    print(f"{operator} is an invalid operator")