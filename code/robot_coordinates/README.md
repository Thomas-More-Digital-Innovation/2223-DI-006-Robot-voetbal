# Robot coordinates
An OpenCV software for detecting color ranges and recognizing patterns in color combinations. 

## Introduction
This folder contains the code for retrieving robot car and ball coordinates from video footage. You can easily adapt the code to your own situation. Before you start, you need to mount some collored paper (postips) on the robot cars and you need a ball with a distinctive color compared to the surface.

## How to run?
### install requirements
    pip install -r requirements

### run the example
    python3 exampleCode.py
The software shows 2 windows, the first are the camera images, the second are masked color images. On these windows you see drawn skeletons of the color combinations found.

## Write your own 
### main.py
Here you can write your own code and create your own color combinations. Study the sample code to understand the framework before you start. First you need to initialize the colors, the cars and the ball. If you have a lot of cars, you can make a list for later. 

### var.py
Define the colors in this file by following the previous class structure. You can refine and adjust the color ranges here. The color value is in HSV representation. You can check the detected colors in the masked window when you run your code.

## Framework
### roboCarTracer.py
This framework does most of the processing. It can extract cars and balls from images based on their colors. Be sure to install its dependecies (opencv-python and numpy).
#### Color()
    red = Color(lower_val ,upper_val)
- lower_val: the minimum HSV value treshold
- upper_val: the maximum HSV value treshold
- This Color object contains a value set of colors.
    
    red.create_mask(frame)
- frame: when passed a frame in this function, it will generate a mask with its colors.

#### Car()
    goalie = Car(color_1, color_2)
- color_1 & color_2: both parameters need to be color objects 
####
    goalie.get_coordinate_angle(frame) -> return coord, angle
- frame: this parameter must be a frame of the video footage
- coord: a tuple containing the x and y coordinates of the car
- angle: a float that represents the angle of the car in degrees. Front and back depend on the order in which you entered the colors in the object when it was created.
####
    goalie.draw(frame) -> return frame
- frame: this parameter must be a frame of the video footage

#### Ball()
    ball.Ball(color)
- color: this parameter needs an Color object
####
    ball.get_coordinate(frame) -> return coord
- frame: this parameter must be a frame of the video footage
- coord: a tuple containing the x and y coordinates of the car
####
    ball.draw(frame) -> return frame
- frame: this parameter must be a frame of the video footage
