# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#Raspberry_Pi_Assignment_Template)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)

&nbsp;

## Launchpad Part 1

### Assignment Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.

### Evidence 

![Here's your evidence you filthy animal](images/shalalala.gif)


### Code
[Countdown.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/Countdown.py)

### Reflection

Using a for loop for this is the easiest way. To make it count down and not count up make sure you have all three parameters in your for loop and the third one is negative. Also if you want it starting at 10 you're gonna need it to be 11 so it actually prints 10, if that makes sense. 

&nbsp;

## Launchpad Part 2

### Assignment Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.


### Evidence 

![Spain without the a](images/blinky.gif)

### Wiring
aaaa

### Code
[CountdownBlink.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/CountdownBlink.py)

### Reflection

Long leg of LED goes to positive. Turn the LED on and off every half seconds so it does a full blink every second. Have a time.sleep at the end or put it in a while True loop so you can actually see the green LED turn on before the code finishes running. 

&nbsp;

## Launchpad Part 3

### Assignment Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff. Include a physical button that starts the countdown. 

### Evidence 

![button without the on](images/button.gif)

### Wiring
aaaaa

### Code
[CountdownButton.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/CountdownButton.py)

### Reflection

Hypothetically there is probably an easier way to do this asssignment, that being said what I did works. Keep in mind! the "if not button.value" should be changed to "if button.value" and vice versa if you are wiring the button differently, not to ground and to the power pin instead. Also in the future perhaps find a way to code it more cleanly so instead of it checking to see if the button has been pressed every half second, it is able to continuously check, if possible.

&nbsp;

## Launchpad Part 4

### Assignment Description

Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor. Blink a red light each second of the countdown, and turn on a green LED to signify liftoff. Include a physical button that starts the countdown. Actuate a 180 degree servo on liftoff to simulate the launch tower disconnecting.


### Evidence 

![AHHHHHHHHHHHHHHH](images/pain.gif)


### Code
[CountdownServo.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/CountdownServo.py)

### Wiring
aaaaa

### Reflection
The servo was easy enough, just adding a few lines of code. Watch out for the wiring because I accidentally wired the ground wire to 3v3 and it temporarily shorted my pico, didn't fry it though. If you want to do the spicy version where it begins to sweep at 3 seconds the easiest way is to use time.monotonic, but you technically don't have to if you have some crazy if statements and for loops but frankly that's just above my pay grade (I'm not getting paid).



&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Take This You Filthy Animal](raspberry-pi/test.py)
### Test Image
![PinkPanther](images/pink.jpg)
### Test GIF
![Me when engineering](images/lizard-dance.gif)
