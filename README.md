# Cut-the-rope
Mini imitation of the popular game Cut The Rope with 3 levels. Written and run on python2.7

To run this game, download all files into the same folder and run the file *cut_the_rope.py*.

![image](https://user-images.githubusercontent.com/54175817/130040259-802a920e-dd08-463c-acbc-85a3f0f87632.png)

The objective of this game is to get the candy to the bowl at the bottom of the screen, by cutting a rope, as the name suggest, and getting past some obstacles. On the way, there are stars for bonus points. All you have to do is to cut the rope, collect all the stars, burst the bubble and escape traps to reach the bowl in the shortest time possible.

The graphics of the game have been incorporated with the help of an external module, Pygame. It involves real life simulations like gravity and oscillations. We have incorporated the concepts of classes and objects, file handling, exception handling.

## Screen shots of the game 

Initial instructions to the player

![image](https://user-images.githubusercontent.com/54175817/130041640-67e97b7e-42bf-4070-ace3-9d427a4c6e93.png)



Menu selection option

![image](https://user-images.githubusercontent.com/54175817/130041629-3f612619-2cce-486d-a398-35e8e04b9885.png)



Level selection option

![image](https://user-images.githubusercontent.com/54175817/130041602-538de061-b2bd-4987-acd9-56b1c4222fc7.png)



Level 1

![image](https://user-images.githubusercontent.com/54175817/130041580-fd881a33-a9dd-45f0-ba7e-4703ab6c5577.png)



Level 2

![image](https://user-images.githubusercontent.com/54175817/130041556-f156ea3e-75b5-4346-9107-675fbd4711b7.png)



Level 3

![image](https://user-images.githubusercontent.com/54175817/130041536-37da2832-5f9d-4e72-9cbf-aa082c467f28.png)



If game is lost 

![image](https://user-images.githubusercontent.com/54175817/130041505-cae4cf8a-588f-4160-b9f0-2a4fb94b8b1a.png)





## GAME FLOWCHART :
![Screen Shot 2021-08-19 at 2 53 58 PM](https://user-images.githubusercontent.com/54175817/130044252-41c3fd2b-705c-4f73-8041-e0be3aa594c6.png)


## MODULES AND FUNCTIONS USED 

Modules: pygame, math, time modules

.

### Library functions
 
**pygame init()** – to initialize the pygame module.

**mixer.init()** – to initialize the mixer sound options.

**mixer.music.load(file)** – to load the playback music file. 

**mixer.music.play(file)** – to play the music loaded.

**mixer.music.get_busy()** – to check whether the mixer is in use.

**mixer.music.stop()** – to stop playing the playback music.

**surface.blit()** – to render the background object on the screen.

**display.set_mode((x,y))** –to create a window of required size.

**display.set_caption(caption)** –to set the title for the window created.

**display.update()** – to update the screen from time to time.

**time.Clock()** – to have an access to time.

**image.load(image)** – to load the image required as an object.

**pygame.transform.scale(object,(x,y))** – to transform the image to a required size.

**event.get()** – to get the state of various input devices.

**mouse.get_pos()** – to get the position of mouse at any instant of time.

**draw.circle(screen,color,(x,y)\<center>,radius,thickness)** – to draw a circle of required dimension on the screen.

**draw.lines(screen,color,closed<True/False>,pointlist,thickness)** – to draw lines on the screen.

**quit()** – to exit from the window created.

**math.sin(angle)** – to obtain sine of an angle.

**math.cos(angle)** – to obtain cosine of an angle.

**time. sleep()** – to make the delay.

.

### User defined functions 
**Sound()**: It takes no parameters. It is evoked to control the play back music options such as on and off.
  
**Menu()**: It takes no parameters. It is evoked to control and to facilitate the main menu options such as play and quit.
  
**LevelSelect()**: It takes no parameters. It is evoked to control and facilitate the level selection options.
  
**swing()**: It takes 6 parameters. It is responsible for the swinging action of the candy. It returns the angle with vertical, tangential velocities of the candy and the new position of candy each time this function is invoked.
  
**Result()**: It takes 1 parameter. This function calculates the score and displays the number of stars collected if won. If lost , allows you to try again .
  
**Fall()**: It takes 13 parameters in which 3 are default parameters. This function takes the responsibility of motion of candy after being cut. It takes care of the normal freefall after being cut ,the bubble floating up, checking whether the bubble gets popped, checking for stars and check whether the bowl has been reached or whether the target has been missed. It returns a Boolean value True or False whether the target has been reached or not .
  
**check_star()**: It takes 2 parameters. This is a function that checks whether the star has been caught by the candy or not. It does not return any value.

**cut()**: It takes 4 parameters. This function checks whether the rope of the candy has been cut or not. It returns a Boolean value True if cut, otherwise False.
  
**Game_Loop()**: It takes 9 parameters. This function is the main game loop that handles the levels of the game. It does not return any value.
  
**render_textrect()**:  Returns a surface containing the passed text string, reformatted to fit within the given rectangle , word-wrapping as necessary. The text  will be anti-aliased.
  
  
  
## SYSTEM REQUIREMENTS :

### Hardware Requirements:
Pentium processor/higher with 2 GB RAM
Mouse
Keyboard
Colour monitor

### Software Requirements:
Operating system – Windows XP or higher
Python version 2.7.4 or higher
3D OpenGL compatible graphics accelerator card.
256 MB RAM.
500 Mhz Pentium 3 processor.
### Recommendations:
A late-model 3D OpenGL compatible graphics accelerator card from nVidia, ATI, 3Dlabs or similar.
512 MB RAM (768 MB or 1 GB preferred).
3 Ghz Pentium 4 processor or similar.

