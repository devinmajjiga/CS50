# ask
answer = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ")
answer = answer.lower()
# answer
match answer:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")