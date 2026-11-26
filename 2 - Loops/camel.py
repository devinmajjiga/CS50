def main():
    camelCase = input('camelCase: ')
    camelCase = snake_case_it(camelCase)

def snake_case_it(camelCase):
    print(f"snake_case: ", end="")
    for c in camelCase:
        if c.isupper():
            print(f"_{c.lower()}", end="")
        else:
            print(c, end="")

main()