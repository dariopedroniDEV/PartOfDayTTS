# Input box for selecting language. Numbered value automatically converted to integer varaible.

class lanInput:
    lanInt = int(input("Language/Lingua/Språk: \n 1.English \n 2.Italiano \n 3.Norsk \n"))
    if lanInt == 1:
        lanVal = 'en'
    if lanInt == 2:
        lanVal = 'it'
    if lanInt == 3:
        lanVal = 'no'
    if lanInt >= 4:
        print('Invalid number!')

# Trying to figure out how to use GetText...
lanFile = 'idk'


