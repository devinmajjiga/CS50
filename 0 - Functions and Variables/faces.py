def main():
    # ask what they want to say
    word = input("What would you like to say? ")
    #convert it
    word = convert(word)
    #print it
    print(word)


def convert(happy):
    #replace happy face
    happy = happy.replace(":)","🙂")
    # replace sad face
    happy = happy.replace(":(","🙁")
    # return string
    return happy


# do it
main()
