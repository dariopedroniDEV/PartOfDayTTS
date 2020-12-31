# Initializing variables
lanCheck = 0


# Language selection loop. If incorrect value is entered then it will ask again for language.
def lanInput():
    global lanVal
    while lanCheck == 0:
        lanInt = int(input("Language/Lingua/Språk: \n 1.English \n 2.Italiano \n 3.Norsk \n"))
        if lanInt == 1:
            lanVal = 'EN'
            print("English selected.")
            lanCheck == 1
            break

        elif lanInt == 2:
            lanVal = 'IT'
            print("Lingua Italiana selezionata.")
            lanCheck == 1
            break


        elif lanInt == 3:
            lanVal = 'NO'
            print("Norsk valgt.")
            lanCheck == 1
            break

        else:
            print('Invalid number!')
# Now all strings will end with the proper lanVal
lanInput()

helloNO = "Dette er i norsk!."
helloIT = "Questo testo è scritto in Italiano."
helloEN = "This text is written in English."

helloSTR = 'hello'+lanVal
print(helloSTR)