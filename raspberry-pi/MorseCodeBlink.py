import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP18)
led.direction = digitalio.Direction.OUTPUT

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier #Creates all the variables for the morse code spacing, with the proper ratios, which can be changed evenly in length by changing the modifier

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
        '(':'-.--.', ')':'-.--.-', '\'':'.----.' } #Sets up the library to be used with the morse code, with every common character having the corresponding morse letter

    message = input("Type in here lol:     ") #Asks for input and prints "Type in here lol:"
    if message == "-q": #Checks if user has quit program by typing "-q"
        break #Breaks if user has typed "-q"
    for char in message: #Begins for loop which loops through the same number of times as the character (char) in the user input
        if char == " ": #Checks if a a character is a space (could also be moved to dictionary in hindsight)
            morseOutput += "/" #Adds a forward slash to string if character is a space
        else: 
            morseOutput += MORSE_CODE[char.upper()] + " " #Adds corresponding morse characters for every input character to the string
    print(morseOutput) #Prints final morse string
    for char in morseOutput: #Another for loop based on characters, this time from the morse output
        if char == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(between_taps)
        if char == "-":
            led.value = True
            time.sleep(dash_time)      #All of these are variations on the same couple lines, checking the character, turn the LED on/off
            led.value = False          #for the specified amount of time according to the variables
            time.sleep(between_taps)
        if char == " ":
            led.value = False
            time.sleep(between_letters)
        if char == "/":
            led.value = False
            time.sleep(between_words)

