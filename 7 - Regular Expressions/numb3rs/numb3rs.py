import re

def main():
    ip = input("IPv4 Address: ")
    ip = validate(ip)
    print(ip)

def validate(ip):
    while True:
        if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
                for i in range(4):
                    i = i + 1
                    if not number_validation(matches.group(i)):
                         return False
                    if i == 4:
                        return True
        else:
            return False

def number_validation(number):
    if number == "0":
        return True
    elif int(number) <= 255:
         for digit in str(number):
              if int(digit) == 0:
                   return False
              else:
                   return True
    else:
         return False

if __name__ == "__main__":
    main()