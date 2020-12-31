
# Language selection loop. If incorrect value is entered then it will ask again for language.
def lanInput():
    lanInt = int(input("Language/Lingua/Språk: \n 1.English \n 2.Italiano \n 3.Norsk \n"))
    while lanCheck == 0:

        if lanInt == 1:
            lanVal = 'en'
            print("English selected.")
            lanCheck == 1

        if lanInt == 2:
            lanVal = 'it'
            print("Lingua Italiana selezionata.")
            lanCheck == 1


        if lanInt == 3:
            lanVal = 'no'
            print("Norsk valgt.")
            lanCheck == 1

        else:
            print('Invalid number!')




lanInput()
print("lanInput exited properly.")


# Trying to figure out how to use GetText...
# Maybe NullTranslations can be useful?
# Screw this, I`ll do it my own way
# Totally off topic, but in Python 2.7 you could execute some pretty dangerous commands through the input function, if running through Sudo. For example you could remove OS files.



