import cv2
import numpy as np
from roboCarTracer import Tracer, Color, ColorObject


def main():
    # start capturing the webcam
    cam = cv2.VideoCapture(0) 

    # set capturing resolution
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # set the mask filter colors
    color_team_1 = Color(np.array([90, 100, 50]), np.array([130, 255, 255]), 'blue')
    color_team_2 = Color(np.array([160, 50, 50]), np.array([200, 255, 255]), 'pink')
    color_player = Color(np.array([0, 125, 0]), np.array([30, 255, 255]), 'yellow')
    color_ball = Color(np.array([0, 180, 50]), np.array([15, 255, 255]), 'orange')
    all_colors_list = [
        color_team_1, 
        color_team_2, 
        # color_player, 
        # color_ball
        ]

    # for each frame
    while True:

        # read webcam
        ret, frame = cam.read() 

        for color in all_colors_list:
            # apply the mask filter color on the frame
            color.create_mask(frame)
    
            # get and set coordinates of all found objects
            color.contours = Tracer.get_contours(color.mask)

            # get the center point of every contour
            center_points_list = Tracer.get_contours_center_point(color.contours)

            # set all found color objects
            for center_point in center_points_list:
                ColorObject(color.color, center_point)
                frame = Tracer.draw_center_point(frame, center_point)

        # display cam
        cv2.imshow('Webcam', frame)
        
        # filter = cv2.bitwise_and(frame, frame, mask=team_A_filter.mask)
        # cv2.imshow('masked', filter)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit

    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()