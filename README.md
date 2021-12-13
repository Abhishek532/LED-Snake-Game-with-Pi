# Snake Game

 Play the retro snake game on an 8x8 LED matrix controlled by the Raspberry Pi!

# How it works
The game works on an 8x8 LED matrix that is connected to the GPIO of the Raspberry Pi, which runs the script for the game. The Pi takes input from a **USB keyboard** connected to it and the snake moves according to the input given (Up, Down, Left, Right). If the snake collides into itself, it dies and the score is displayed on a 7 segment display connected to the Pi. 

# Libraries 

RPi.GPIO is the standard go-to library to control the GPIO on a Raspberry Pi because of it's ability to handle inputs in real time. It is a powerful library that gives easy control over the GPIO.

# Gallery

### The complete setup
![IMG_20190419_003537](https://user-images.githubusercontent.com/42097564/116365500-ed636280-a822-11eb-8d9c-78102c854aab.jpg)


![IMG_20190419_040434](https://user-images.githubusercontent.com/42097564/116364265-a759cf00-a821-11eb-80ba-0ca032faf98d.jpg)

### GPIO Pin Diagram
![Screenshot_20190419-001928](https://user-images.githubusercontent.com/42097564/116364309-b3459100-a821-11eb-8a7a-c163d18dd0c7.jpg)

### Videos
#### 7 Segment functioning
https://user-images.githubusercontent.com/42097564/116364343-bb9dcc00-a821-11eb-94f1-d5213069ce71.mp4

#### The snake in action
https://user-images.githubusercontent.com/42097564/116364464-da9c5e00-a821-11eb-8b8f-c9f1cb3f8eec.mp4

