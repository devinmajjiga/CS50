import inflect
names = []

while True:
    try:
        name = input('Name: ')
    except KeyboardInterrupt:
        print("")
        break
    except EOFError:
        break
    names.append(name)

names = inflect.engine().join(names, conj="and")

print(f"Adieu, adieu, to {names}")