def main():
    print(f"Amount Due: 50")
    amount_due = 50
    while True:
        money = int(input("Insert coin: "))
        if money == 5 or money == 10 or money == 25:
            pass
        else:
            money = 0
        amount_due = amount_due - money
        if amount_due <= 0:
            print(f"Change Owed: {amount_due + -2 * amount_due}")
            break
        print(f"Amount Due: {amount_due}")
    


main()
