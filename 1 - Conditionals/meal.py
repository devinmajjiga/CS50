def main():
    time = input("What is the time? ")
    time = convert(time)
    print(time)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

def convert(time):
    def timetonumber(time, x = 0):
        (hours, minutes) = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        float(x)
        if minutes >= 60 or hours > 24:
            print("Please use a real time")
        minutes = minutes / 60.00
        return hours + minutes + x
    if time.endswith("p.m."):
        time = time.replace("p.m.","")
        time = timetonumber(time, 12)
        if 24 <= time < 25:
            time = time - 12
        return float(time)
    elif time.endswith("a.m."):
        time = time.replace("a.m.","")
        time = timetonumber(time)
        return float(time)
    else:
        time = timetonumber(time)
        return float(time)

if __name__ == "__main__":
    main()