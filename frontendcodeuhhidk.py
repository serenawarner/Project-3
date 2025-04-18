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

    i = "00"

    


    # checks for recognized command

    # if opener == "file":
    #     if syntax1 == "starred":
     #       if syntax2 ==