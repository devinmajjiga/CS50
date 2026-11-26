from datetime import date
import sys
import re
import inflect


def main():
    birth = input("Date of Birth: ")
    try: 
        birth = check_birth(birth)
    except ValueError:
        sys.exit("Invalid date")
    minutes = time_of(birth)
    print(minutes)


def check_birth(birth):
    if matches := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth):
        years = int(matches.group(1))
        months = int(matches.group(2))
        days = int(matches.group(3))
        if not 0 < years <= 9999:
            raise ValueError("Invalid Year")
        if not 0 < months <= 12:
            raise ValueError("Invalid Month")
        if not 0 < days <= 31:
            raise ValueError("Invalid Day")
    else:
        raise ValueError
    return date(years,months,days)


def time_of(birth):
    today = date.today()
    years = birth.year
    months = birth.month
    days = birth.day
    bday = date(years, months, days)
    age = today - bday
    age = age.total_seconds()
    minutes = age/60
    minutes = int(minutes)
    minutes = inflect.engine().number_to_words(minutes)
    minutes = re.sub(r" and ", " ", minutes)
    phrase = f"{minutes.capitalize()} minutes"
    return phrase


if __name__ == "__main__":
    main()