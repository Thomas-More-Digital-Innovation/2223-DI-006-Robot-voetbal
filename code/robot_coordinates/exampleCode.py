import cv2
from var import Blue, Pink, Orange
from roboCarTracer import Color, Car, Ball


def main():

    '''
    Here you have some example code of how to define objects and look for them on the incomming video footage.
    For more information, check the README.md
    '''
    
    # set all the colors
    blue = Color(Blue.LOWER_VAL.value, Blue.UPPER_VAL.value)
    pink = Color(Pink.LOWER_VAL.value, Pink.UPPER_VAL.value)
    orange = Color(Orange.LOWER_VAL.value, Orange.UPPER_VAL.value)

    # set all the objects
    # team 1
    team_1_striker_1 = Car(blue, orange)

    # team 2
    team_2_striker_1 = Car(pink, orange)

    # car list
    car_list = [
        team_1_striker_1,
        team_2_striker_1
    ]

    # ball
    ball = Ball(blue)

    # for each frame
    while True:

        # read webcam
        ret, frame = cam.read() 
        if ret:
            general_mask = 0

            for car in car_list:
                # extract car locations from frame
                car.get_coordinate_angle(frame)
                
                # create a general mask of all detected car colors
                general_mask += car.color_1.mask
                general_mask += car.color_2.mask

                # draw on the original frame the skeleton of the cars (for visual confirmation)
                frame = car.draw(frame)

            # do the same for the bal (initialization)
            ball.get_coordinate(frame)
            general_mask += ball.color.mask
            frame = ball.draw(frame)
                
            # create a filtered frame with the general mask
            filtered_frame = cv2.bitwise_and(frame, frame, mask=general_mask)

            # display cam
            cv2.imshow('Webcam', frame)
            cv2.imshow('Masked', filtered_frame)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit

    cv2.destroyAllWindows()


if __name__ == '__main__':
    # start capturing the webcam
    cam = cv2.VideoCapture(0) 

    # set capturing resolution
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    main()
