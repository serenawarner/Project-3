i = "0"
while i != "00":
    
    # generates array of command and syntaxes

    cmd = input()
    cmdarr = cmd.split(" ")
    opener = cmdarr[0]
    syntax1 = cmdarr[1]
    syntax2 = cmdarr[2]

    #test cases
    print(opener)
    print(syntax1)
    print(syntax2)

    # idiot break
    #i = "00"


    #checks for recognized command

    if opener == "file":
        if syntax1 == "star":
            if syntax2 == "toggle":
                #[FILE STARRED VARIABLE HERE] = ![VARIABLE AGAIN]
                print("changed the star value ^w^") #REMOVE THIS LATER
            if syntax2 == "on":
                #[FILE STARRED VARIABLE HERE] = True
                print("file star value is true now! ^w^") #REMOVE THIS LATER
            if syntax2 == "off":
                #[FILE STARRED VARIABLE HERE] = False
                print("file star value is false now! ^w^") #REMOVE THIS LATER
            else:
                print("syntax error! file true accepts arguments: toggle, on, off")
        else:
            print("syntax error! file accepts arguments: star")
    else:
        print("command unrecognized! commands known: file")
    
print("im in hell")