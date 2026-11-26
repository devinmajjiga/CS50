from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
#fonts list
fonts = figlet.getFonts()
# if users supplies a font
if len(sys.argv) == 3:
    if sys.argv[1] in ["-f","--font"]:
        if sys.argv[2] in fonts:
            f = sys.argv[2]
        else:
            print("invalid usage")
            sys.exit()
    else:
        print("invalid usage")
        sys.exit()
#chooses a random fonr
elif len(sys.argv) == 1:
    f = random.sample(fonts,k=1)
    f = str(f)
    f = f.strip("[]")
    f= f.strip("""''""")
#if user does something else
else:
    print("invalid usage")
    sys.exit()
#ask and print
text = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(text))