#ask
expression = input("Expression: ")
expression = expression.strip()
(x,y,z) = expression.split(" ")

#make integers
x = int(x)
z = int(z)

#undefined
if y == "/" and z == 0:
    print("undefined")

#math
match y:
    case "+":
        math = x+z
    case "-":
        math = x-z
    case "*":
        math = x*z
    case "/":
        math = x/z
    case '%':
        math = x%z
    case _:
        print("Use mathematical signs please")


math = round(math, 1)
print(f"{math:.2f}")