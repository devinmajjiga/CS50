def main():
    twitter = input("Input: ")
    twitter = remove_vowels(twitter)


def remove_vowels(twitter):
    print("Output: ", end="")
    vowels = {"a","e","i","o","u","A","E","I","O","U"}
    for c in twitter:
        if c in vowels:
            c = ""
        print(c, end="")

main()