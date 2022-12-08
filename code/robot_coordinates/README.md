# Robot coordinates
An OpenCV software for detecting color ranges and recognizing patterns in color combinations. 

## Introduction
This folder contains the code for retreiving the coordinates of the robot cars and ball from  video footage. Before you start, you need some collered paper (postips) mounted on the robot cars and you need an ball with an outstanding color compared to the underground.

## How to run?
### install requirements
    pip install -r requirements

### run the example
    python3 exampleCode.py
The software will display 2 vensters, the first one is the camera footage, the second one is a color masked footage. On these streams you can see drawn skeletons of the found color combinations.

## Write your own 
### main.py
Here, you can write your own code and create your own color combinations. Examen the example code to understand the framework before you start. First you have to initialize the colors, the cars and the ball. If you have an lot of cars you can choose to create an list for later on. 

After initializing the cars, you can get each car object coordinate via the get_coordinate_angle() function. This function will return 2 value: An tuple with the car coordinates and a float for the angle in degrees. These values are also stored in the object variables self.coord and self.angle. You can also draw the car skeleton on the fram via the draw() function. You will pass the frame in the function parameter and it will return a new frame with drawing.

### var.py
Define colors in the this file by following the previous class structure. You can finetune and tweak the color ranges here. The color value is in HSV representation. You can check the detected colors in the masked venster.

### Framework (roboCarTracer.py)
#### Color()
    red = Color(lower_val ,upper_val)
lower_val: the minimum HSV value treshold
upper_val: the maximum HSV value treshold
This Color object contains a value range of colors.

    red.create_mask(frame)
frame: when passed a frame in this function, it will generate a mask with its colors.

#### Car()
    goalie = Car(color_1, color_2)
color_1 & color_2: both parameters need to be color objects 

    goalie.get_coordinate_angle(frame) -> return coord, angle
frame: this parameter needs to be a frame of the video footage
coord: a tuple containing the x and y coordinates of the car
angle: a float that represents the angle of the car in degrees. Front and back depend on the order you input the colors in the object when it was created.

    goalie.draw(frame) -> return frame
frame:

#### Ball()
    ball.Ball(color)
color:

    ball.get_coordinate(frame) -> return coord
frame:
coord:

    ball.draw(frame) -> return frame
frame:
