def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else: 
        print("Invalid")


def no_middle_numbers(plate):
    if plate.isalpha():
        return True
    for i in plate:
        if i.isnumeric():
            (trash, alpha) = plate.split(i, maxsplit=1)
            if alpha.isnumeric():
                return True


def no_0_first(plate):
    if plate.isalpha():
        return True
    for c in plate:
        if c.isnumeric():
            if c == "0":
                return False
            else:
                return True


def starts_with_two_letters(plate):
        if plate[0:2].isalpha():
            return True
        else:
            return False


def no_special_characters(plate):
    if plate.isalnum():
        return True
    else:
        return False


def is_length_correct(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False


def is_valid(plate):
    if is_length_correct(plate) and no_special_characters(plate) and starts_with_two_letters(plate) and no_0_first(plate) and no_middle_numbers(plate):
        return True
    else:
        return False


if __name__ == "__main__":
    main()