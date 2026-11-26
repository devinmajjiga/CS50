import sys

def main():
    check_arg(sys.argv)
    try:
        user_file = sys.argv[1]
    except IndexError:
        pass
    lines = find_line_amount(user_file)
    print(lines)

def check_arg(arg):
    if len(arg) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif len(arg) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif not arg[1].lower().endswith(".py"):
        print("Not a Python file")
        sys.exit()

def find_line_amount(user_file):
    try:
        line_amount = 0
        with open(user_file, "r") as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#"):
                    line_amount +=0
                    continue
                for c in line:
                    if not c in " ":
                        line_amount += 1
                        break
    except FileNotFoundError:
        print("File does not exist")
    return line_amount

if __name__ == "__main__":
    main()