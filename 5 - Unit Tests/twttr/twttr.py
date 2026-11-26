def main():
    twitter = input("Input: ")
    twitter = shorten(twitter)


def shorten(twitter):
    print("Output: ", end="")
    vowels = {"a","e","i","o","u","A","E","I","O","U"}
    sentence =[]
    for c in twitter:
        if c in vowels:
            c = ""
        sentence.append(c)
    return "".join(sentence)

if __name__ == "__main__":
    main()