import re
import sys

def main():
    text = input("Text: ")
    text = count(text)
    print(text)

def count(text):
    matches = re.findall(r"\bum\b", text, re.IGNORECASE)
    matches = len(matches)
    return matches

if __name__ == "__main__":
    main()