import re

def main():
    html = input("HTML: "  )
    html = parse(html)
    print(html)

def parse(html):
    if matches := re.search(r"(https?://)?(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)", html):
        link = matches.group(3)
        link = f"https://youtu.be/{link}"
        return link
    else:
        return "None"

if __name__ == "__main__":
    main()