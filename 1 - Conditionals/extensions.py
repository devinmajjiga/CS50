#ask
file = input("File name: ")
file = file.lower()
file = file.strip()
todo = "todo"
#.gif
if file.endswith(".gif"):
    print("image/gif")
#.jpg and jpeg
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
#.png
elif file.endswith(".png"):
    print("image/png")
#.pdf
elif file.endswith(".pdf"):
    print("application/pdf")
#.txt
elif file.endswith(".txt"):
    print("text/plain")
#.zip
elif file.endswith(".zip"):
    print("application/zip")
#other
else:
    print("application/octet-stream")