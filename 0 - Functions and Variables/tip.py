def main():
    dollars = (input("How much was the meal? "))
    percent = (input("what percentage would you like to tip? "))
    dollars = dollars_to_float(dollars)
    percent = percent_to_float(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(money):
    money = money.replace("$","")
    money = float(money)
    return money

def percent_to_float(p):
    p = p.replace("%","")
    p = float (p)
    p = p / 100
    return p

main()