grocery_list = {}
while True:
    try:
        item = input()
    except (KeyboardInterrupt, EOFError):
        for item in sorted(grocery_list):
            print(f"""{grocery_list[item]} {item}""")
        break
    item = item.upper()
    item = item.strip()
    if item in grocery_list.keys():
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1