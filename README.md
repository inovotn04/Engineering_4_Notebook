# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad Part 1](#launchpad-part-1)
* [Launchpad Part 2](#launchpad-part-2)
* [Launchpad Part 3](#launchpad-part-3)
* [Launchpad Part 4](#launchpad-part-4)
* [Crash Avoidance Part 1](#crash-avoidance-part-1)
* [Crash Avoidance Part 2](#crash-avoidance-part-2)
* [Crash Avoidance Part 3](#crash-avoidance-part-3)
* [Landing Area Part 1](#landing-area-part-1)
* [Landing Area Part 2](#landing-area-part-2)
* [Morse Code Part 1](#morse-code-part-1)
* [Morse Code Part 2](#morse-code-part-2)
* [FEA Part 1)(#fea-part-1)

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

![LEDWIRING](images/jusled.jpg)

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

![BUTTONWIRING](images/jusbutton.jpg)

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

![servowiring](images/buttonwservo.jpg)

### Reflection
The servo was easy enough, just adding a few lines of code. Watch out for the wiring because I accidentally wired the ground wire to 3v3 and it temporarily shorted my pico, didn't fry it though. If you want to do the spicy version where it begins to sweep at 3 seconds the easiest way is to use time.monotonic, but you technically don't have to if you have some crazy if statements and for loops but frankly that's just above my pay grade (I'm not getting paid).



&nbsp;

## Crash Avoidance Part 1

### Assignment Description

Create a module that has an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor.


### Evidence 

![wowza](images/accelgif.gif)


### Code
[Accelerometer.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/Accelerometer.py)

### Wiring

![Accelwire](images/Accelwire.jpg)

### Reflection
Wiring was super easy it's weird that you only wire one side of the accelerometer though. As far as the code goes I think the f string is easiest for printing. You may not have to slap the mpu inputs into variables and you could directly pull into the print string but I haven't tried it and frankly I am too scared to, but it could save you a couple lines of code. Don't be alarmed by your z variable printing ~9.8 that's just gravity.


&nbsp;

## Crash Avoidance Part 2

### Assignment Description

Create a module that has an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source. 


### Evidence 

![Spam (like the meat)](images/powergif.gif)


### Code
[AccelerometerLED.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/AccelerometerLED.py)

### Wiring

![AcceLED](images/AcceLED.jpg)

### Reflection
This assignment was actually dead easy. Everything worked perfectly the first time. I think I could maybe give you advice in terms of find the right value for the if statement to check whether it's 90 degrees, personally mine was pretty jumpy so I set it to 1 for the z variable.


&nbsp;

## Crash Avoidance Part 3

### Assignment Description
Create a module that has an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor. The module must have an LED that turns on if the helicopter is tilted to 90 degrees. The module must be powered by a mobile power source. The module must have an onboard screen that prints x, y, and z angular velocity values (rad/s) rounded to 3 decimal places.


### Evidence 

![bush did 9/11](images/disgif.gif)


### Code
[AccelerometerDisplay.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/AccelerometerDisplay.py)

### Wiring

![AccelDis](images/AccelDis.jpg)

### Reflection
This was pretty challenging, in terms of getting the wiring to work and working with the pretty finicky code. Main thing to remember is that i2c wiring is always off of two pins, this does however mean the coding is a bit harder because you have to put in the address in a long initialization statement for each device. Also make sure to use the code to find the addresses of the devices, and if you're not finding them try reconnecting and checking wiring.

&nbsp;

## Landing Area Part 1

### Assignment Description
Create a program which calculates the area of a triangle. The code must ask for the user to input a set of three coordinates in (x,y) format. The triangle area must be determined using a function. If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script. The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km. The code must return to the input stage after printing the area, and wait for user input.



### Evidence 

![wowza](images/trianglegif.gif)


### Code
[triangleArea.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/triangleArea.py)


### Reflection
The split function formats the output as a list, so to access it you need to do _your output name_[_number of item in list_]. For example if I did 
```python
txt = "69, 420"
output = txt.split(, )
```
I would have to access one of those numbers by saying
```python
x = output[1]
```
to get the number "420." Other than that, using 'try' and 'except' is actually astoundingly simple and horrifically helpful so it's important to use that. The only other problem was the way I formatted my math statement. Python doesn't recognize 'a(b)' as multiplication so you have to format that as 'a*(b)' and that caught me up for a while.

&nbsp;

## Landing Area Part 2

### Assignment Description

Create a program which calculates the area of a triangle. The code must ask for the user to input a set of three coordinates in (x,y) format. The triangle area must be determined using a function. If the user inputs coordinates incorrectly (letters or improper format) the code should return to the input stage, it should not throw an error or exit the script. The triangle area must be printed to the screen in this format: “The area of the triangle with vertices (x,y), (x,y), (x,y) is {area} square km. The code must return to the input stage after printing the area, and wait for user input. An onboard OLED screen must plot each triangle on a graph relative to the base location.

### Evidence 

![inlineienei](images/tridisplay.gif)

### Wiring

![displaywire](images/displaywire.jpg)

### Code

[triangleDisplay.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/triangleDisplay.py)

### Reflection
This one is literally just adding a display. I guess like remember the coordinates have 64, 32 as the center. That part actually caused me problems after the fact, so you gotta like do weird math and divisions and stuff. So do those divisions! Like  when you write it, because doing it after the fact is harder and feels more tedious.

&nbsp;

## Landing Area Part 3

### Assignment Description

Create a program which calculates the area of a triangle. A list of coordinates must be hard coded into the script. The triangle area must be determined using a function. The code must select the triangle with the closest centroid that has an area > 100 km^2. An onboard screen must plot each triangle as it is evaluated on a graph relative to the base. The code must print the following text “The closest suitable landing area has vertices ({x}, {y}, {z}). The area is {area} km2 and the centroid is {distance} km away from base."

### Evidence 

![spicyicy](images/spicyicy.gif)

### Wiring
![displaywire](images/displaywire.jpg)

### Code

[triangleCentroid.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/triangleCentroid.py)


### Reflection
There's a lot of things to say about this. Firstly, put your calculation for the triangle center and the triangle area in two different function. If you don't do this you'll have to do so many lists and other stuff. Furthermore in the end it probably will not work at all, or at least that's what I discovered. If you feel like making more work for yourself then put it all in one function, see if I care.


&nbsp;

## Morse Code Part 1

### Assignment Description

Create a which accepts text input by the user. If the user types “-q”, your script must exit. If the user types anything else, your script must translate the text to morse code dots and dashes, and print those to the monitor. The printed text must use a space to show breaks between letters, and a slash to show breaks between words


### Evidence 

![morse](images/morse.gif)

### Code

[MorseCode.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/MorseCode.py)


### Reflection
This code went really smoothly. Like from start to finish. It must be said that the way I started coding it was really janky, like not using the dictionary correctly. Using the dictionary correctly you only need ONE line of code to tell it to parse through the message and convert it to morse code. If you were doing it incorrectly then you have a bunch of if statements checking the characters and it's like 100 lines of code, and what's even the point of using the dictionary if you're doing that?


&nbsp;

## Morse Code Part 2

### Assignment Description

Create a which accepts text input by the user. If the user types “-q”, your script must exit. If the user types anything else, your script must translate the text to morse code dots and dashes, and print those to the monitor. The printed text must use a space to show breaks between letters, and a slash to show breaks between words. The script must flash an LED to transmit the morse code message using the timing sequence shown below

### Evidence 

![morse](images/morse.gif)

### Wiring
![wireman](images/LEDwire.jpg)

### Code

[MorseCodeBlink.py](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/raspberry-pi/MorseCodeBlink.py)


### Reflection
You know how to make an LED blink. Do that. Then you just do a for loop and a bunch of if statements for the dots and dashes. It's simple. It's so horrendously simple. I don't know how to reflect on this. I think I made it a bit less efficient by adding extra 'led.value(False)' lines that didn't need to be there so maybe get rid of those if you feel like it. That's all.


&nbsp;

## FEA Part 1

### Assignment Description

Making a 180 mm long PLA 3d printed beam intended to hold the most amount of weight without breaking or bending past 35 mm. It must also not weigh more than 13 grams and work fully with the provided materials (attachment block and the bolt to hang weight off of). 


### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/b0642ff49d8db9b862992a16/w/256263874c5873489822cbff/e/eb74407b2954334966743e40?renderMode=0&uiState=6413215471e8f942da5b5753).

### Part Image

![Image](https://github.com/bwright70/RasberryPiPico/blob/main/images/Beam%20Design%201.png)

Image courtesy to
[Ben Wright](https://github.com/bwright70/RasberryPiPico)

### Reflection

There are many things which one can say went wrong with this assignment. In my infinite wisdom, when my partner Ben was absent, I designed this beam to include as many triangles as possible, because hey that sounds structurally sound. It had the right idea but unfortunately I forgot that they sort of have to be connected in order to add any benefits. Needlessly to say our beam immediately broke. So consider whether a design logically makes sense before you just make the coolest thing possible.

&nbsp;


## FEA Part 2

### Assignment Description

Use simscale to run an FEA analysis on the beam we just created. This is the Finite Element Analysis of the FEA assignment.


### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/b0642ff49d8db9b862992a16/w/256263874c5873489822cbff/e/eb74407b2954334966743e40?renderMode=0&uiState=6413215471e8f942da5b5753).

### Part Image

![Image](https://github.com/bwright70/RasberryPiPico/blob/main/images/Beam%20Simulation.png)

Image courtesy to
[Ben Wright](https://github.com/bwright70/RasberryPiPico)

### Reflection

So after creating the mesh and trying to simulate a weight on the beam, there was some error in simscale, likely due to what a weird part we created, which meant we had to change some setting to override it and let us simulate. After simulating it was very apparent that the beam was awful and would immediately break, however it was easy to ignore that and blame that on the setting we changed. In the above image, displacement is not turned on, if it was on then the beam would like gumby being used to hold together a tractor trailer. Long story short we should've changed a lot more before the physical test but I'll get to that in the next part.

&nbsp;


## FEA Part 3

### Assignment Description

After running FEA, use the data collected to improve the design of our beam and decrease the maximum stress by half of what it was originally.


### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/b0642ff49d8db9b862992a16/w/256263874c5873489822cbff/e/eb74407b2954334966743e40?renderMode=0&uiState=6413215471e8f942da5b5753).

### Part Image

![Image](https://github.com/bwright70/RasberryPiPico/blob/main/images/Beam%20Design%202.png)

Image courtesy to
[Ben Wright](https://github.com/bwright70/RasberryPiPico)

### Reflection

So we did in fact make design changes after the horrific simulation. We added those little supporting diamonds in between that triangles which you can see in the image, and also generally optimized the part. This didn't change the main problem that the triangles were completely unconncected at the top which ultimately came back to haunt us when we tested it in the physical realm. It did in fact decrease the deflection and stress significantly though, but the design itself was still very flawed. 

&nbsp;

## Ring and Spinner

(I made the spinner)

### Assignment Description

Using Onshape, create the first part of a CAD model representing one of those spinny flying propeller things. I created the "spinner" part which slots into the propeller and create the rack and pinion relationship between the key to make it spin. The parts must have the measurements specified in the assignment. 


### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/cefa2f1ec2fa9e5464d39714/w/7ba99138f933b01dea9e2b36/e/b0646f7597741d74c99b2536).

### Part Image

![Image](https://github.com/inovotn04/Engineering_4_Notebook/blob/main/images/Spinner.png)

### Reflection

I have nothing to write here. If anything the biggest lesson is  to write your reflections right after you finish the assignment, so you can actually have something to write. Nobody will read this but you though, it doesn't matter. My knowledge, my experience, is carried on through words and words, themselves, are carried on through their own meaning. We're taught this meaning through others. I am one of those others, persisting the meaning of these words, and these words are persisting the story of my own life. You are the sole proprietor now of a piece of my being, and the judge and jury, deciding what that means to you.

&nbsp;




## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Take This You Filthy Animal](raspberry-pi/test.py)
### Test Image
![PinkPanther](images/pink.jpg)
### Test GIF
![Me when engineering](images/lizard-dance.gif)
