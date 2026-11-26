import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        answer = a + b
        for j in range(4):
            if j == 3:
                print(f"{a} + {b} = {answer}")
            else:
                try:
                    user_answer = int(input(f"{a} + {b} = "))
                except ValueError:
                    print("EEE")
                    continue
                if int(user_answer) == answer:
                    score = score + 1
                    break
                else:
                    print("EEE")

    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        try:
            if int(level) in [1,2,3]:
                return int(level)
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    if level == 2:
        return random.randint(10,99)
    if level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
