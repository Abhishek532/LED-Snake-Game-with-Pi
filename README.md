# Snake Game

 Play the retro snake game on an 8x8 LED matrix controlled by the Raspberry Pi!

# How it works
The game works on an 8x8 LED matrix that is connected to the GPIO of the Raspberry Pi, which runs the script for the game. The Pi takes input from a USB keyboard connected to it and the snake moves according to the input given (Up, Down, Left, Right). If the snake collides into itself, it dies and the score is displayed on a 7 segment display connected to the Pi. 

# Libraries 

RPi.GPIO is the standard go-to library to control the GPIO on a Raspberry Pi because of it's ability to handle inputs in real time. To control the 8x8 LED matrix 

