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
between_words = 7*modifier

while True:

    morseOutput = ""
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
        '(':'-.--.', ')':'-.--.-', '\'':'.----.' }

    message = input("Type in here lol:     ")
    if message == "-q":
        break
    for char in message:
        if char == " ":
            morseOutput += "/"
        else:
            morseOutput += MORSE_CODE[char.upper()] + " "
    print(morseOutput)
    for char in morseOutput:
        if char == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
            time.sleep(between_taps)
        if char == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False
            time.sleep(between_taps)
        if char == " ":
            led.value = False
            time.sleep(between_letters)
        if char == "/":
            led.value = False
            time.sleep(between_words)

