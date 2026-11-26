def main():
    fraction = fraction_to_percent("Fraction:")
    if fraction <= 1:
        print("E")
    elif 99 <= fraction:
        print("F")
    else:
        print(f"{fraction}%")



def fraction_to_percent(prompt):
    while True:
        try:
            fraction = input(prompt)
            (x,y) = fraction.split("/")
            x = int(x)
            y = int(y)
            fraction = x / y
            if fraction < 0 or fraction > 1:
                continue
            percent = float(fraction) * 100
            percent = int(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return percent


main()