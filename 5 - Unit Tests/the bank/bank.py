def main():
    greeting = input("Greeting: ")
    money = value(greeting)
    print(money)

def value(greeting):
    #strip
    greeting = greeting.strip()
    #no case
    greeting = greeting.lower()
    #is it hello
    if greeting.startswith("hello"):
        return "0$"
    elif greeting.startswith("h"):
        return "20$"
    else:
        return "100$"

if __name__ == "__main__":
    main()