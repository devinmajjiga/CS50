months_of_the_year = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def main():
    while True:
        date = input("Date: ")
        date = date.strip()
        date = date.title()
        try:
            if "/" in date:
                (month, day, year) = date.split("/")
                year = int(year)
                if year < 0:
                    continue
                month = int(month)
                if month > 12 or month < 1:
                    continue
                day = int(day)
                if day > 31 or day < 1:
                    continue
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                (month, day, year) = date.split(" ")
                if month in months_of_the_year:
                    month = months_of_the_year[month]
                else:
                    continue
                year = int(year)
                if year < 0:
                    continue
                month = int(month)
                if month > 12 or month < 1:
                    continue
                if "," not in day:
                    continue
                day = day.replace(",", "")
                day = int(day)
                if day > 31 or day < 1:
                    continue
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            continue


main()
