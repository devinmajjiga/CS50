from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
    check_arg(sys.argv)
    shirt_on_photo(sys.argv[1], sys.argv[2])

def check_arg(arg):
    if len(arg) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(arg) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif not check_endings(arg, 1):
        print("Invalid input")
        sys.exit()
    elif not check_endings(arg, 2):
        print("Invalid input")
        sys.exit()
    trash, ext1 = os.path.splitext(arg[1].lower())
    trash, ext2 = os.path.splitext(arg[2].lower())
    if ext1 != ext2 :
        print("Input and output have different extensions")
        sys.exit()


def check_endings(arg, number: type=int):
    correct_endings = [".jpeg", ".jpg", ".png"]
    for ending in correct_endings:
        if arg[number].endswith(ending):
            return True
        else:
            continue

def shirt_on_photo(input_image, output_image):
    try:
        photo = Image.open(input_image)
        photo = ImageOps.fit(photo, (600, 600), Image.Resampling.BICUBIC, 0.0, (0.5, 0.5))
        shirt = Image.open("shirt.png")
        photo.paste(shirt, mask=shirt)
        photo.save(output_image)
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit()

if __name__ == "__main__":
    main()