import sys
import csv

def main():
    check_arg(sys.argv)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    conversion(input_file, output_file)

def conversion(input_file, output_file):
    try:
        file = open (output_file, "w", newline="")
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        with open(input_file, "r") as file:
            file = csv.DictReader(file)
            for line in file:
                last,first = line['name'].split(",")
                house = line['house']
                with open(output_file, "a", newline="") as file:
                    writer.writerow({"first": first, "last": last, "house": house})
        file.close()
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")

def check_arg(arg):
    if len(arg) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(arg) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif not arg[1].lower().endswith(".csv"):
        print("Not a CSV file")
    elif not arg[2].lower().endswith(".csv"):
        print("Not a CSV file")
        sys.exit()

if __name__ == "__main__":
    main()