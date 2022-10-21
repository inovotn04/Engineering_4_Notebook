

while True:

    morseOutput = "" #Creates empty string to add morse onto

    
    MORSE_CODE = { 'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-', '\'':'.----.' }   #Sets up the library to be used with the morse code, with every common character having the corresponding morse letter

    message = input("Type in here lol:     ") #Asks for input and prints "Type in here lol:"
    if message == "-q": #Checks if user has quit program by typing "-q"
        break #Breaks if user has typed "-q"
    for char in message: #Begins for loop which loops through the same number of times as the character (char) in the user input
        if char == " ": #Checks if a a character is a space (could also be moved to dictionary in hindsight)
            morseOutput += "/" #Adds a forward slash to string if character is a space
        else:
            morseOutput += MORSE_CODE[char.upper()] + " " #Adds corresponding morse characters for every input character to the string
    print(morseOutput) #Prints final morse string
