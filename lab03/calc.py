x = int(input("x = "))
op = input("operation(+,-,*,/): ")
y = int(input("y = "))

a = 0

if op == "+":
    a = x + y
elif op == "-":
    a = x - y
elif op == "*":
    a = x * y
elif op == "/":
    a = x / y
print("*" * 30)
print("{} {} {} = {}".format(x,op,y,a))
print("*" * 30)