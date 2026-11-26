import re
import sys

def main():
    time = input("Hours: ")
    try:
        time = convert(time)
    except ValueError:
        print("Invalid Input")
        sys.exit()
    print(time)

def convert(time):
    if matches := re.search(r"^([\d]{1,2})(:[\d]{2})? (AM|PM) to ([\d]{1,2})(:[\d]{2})? (AM|PM)$", time):
        hours1 = int(matches.group(1))
        hours2 = int(matches.group(4))
        try:
            minutes1 = int(matches.group(2).strip(":"))
        except AttributeError:
            minutes1 = 0
        try:
            minutes2 = int(matches.group(5).strip(":"))
        except AttributeError:
            minutes2 = 0
        bora1 = matches.group(3)
        bora2 = matches.group(6)
        if hours1 <= 12 and hours2 <= 12 and minutes1 <=59 and minutes2 <= 59:
            if bora1 == "PM":
                hours1 = hours1 + 12
                if hours1 == 24:
                    hours1 = 12
            if bora1 == "AM":
                if hours1 == 12:
                    hours1 = 0
            if bora2 == "PM":
                hours2 = hours2 + 12
                if hours2 == 24:
                    hours2 = 12
            if bora2 == "AM":
                if hours2 == 12:
                    hours2 = 0
            if minutes1 == None:
                minutes1 = 0
            if minutes2 == None:
                minutes2 = 0
        else:
            raise ValueError
        return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()