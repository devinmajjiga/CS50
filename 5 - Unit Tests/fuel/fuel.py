def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fraction = convert(fraction)
            fraction = guage(fraction)
            print(fraction)
            break
        except (ValueError, ZeroDivisionError):
             pass


def convert(fraction):
            (x,y) = fraction.split("/")
            x = int(x)
            y = int(y)
            fraction = x / y
            if fraction < 0 or fraction > 1:
                raise ValueError
            fraction = float(fraction) * 100
            fraction = round(fraction)
            fraction = int(fraction)
            return fraction

def guage(fraction):
    if fraction <= 1:
        return "E"
    elif 99 <= fraction:
        return "F"
    else:
        return f"{fraction}%"

if __name__ == "__main__":
    main()