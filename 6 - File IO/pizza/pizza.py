from tabulate import tabulate
import sys
import csv

def main():
    check_arg(sys.argv)
    try:
        user_file = sys.argv[1]
    except IndexError:
        pass
    make_grid(user_file)

def make_grid(user_file):
    try:
        with open(user_file, "r") as file:
            file = csv.DictReader(file)
            output = tabulate(file, headers="keys", tablefmt="grid")
            print(output)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

def check_arg(arg):
    if len(arg) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif len(arg) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif not arg[1].lower().endswith(".csv"):
        print("Not a CSV file")
        sys.exit()

if __name__ == "__main__":
    main()