import cv2
import numpy as np
from var import Team1, Team2, PlayerOffenceOne, PlayerOffenceTwo, PlayerDefence, Ball
from roboCarTracer import Tracer, Color, car


def main():
    # start capturing the webcam
    cam = cv2.VideoCapture(0) 

    # set capturing resolution
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # set the mask filter colors
    color_team_1 = Color(np.array(Team1.LOWER_VAL.value), np.array(Team1.UPPER_VAL.value), Team1.COLOR_STRING.value)
    color_team_2 = Color(np.array(Team2.LOWER_VAL.value), np.array(Team2.UPPER_VAL.value), Team2.COLOR_STRING.value)
    all_colors_list = [
        color_team_1, 
        color_team_2, 
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
            color.color_positions = Tracer.get_contours_center_point(color.contours)

        x = Tracer.compare_distance_center_points(color_team_1.color_positions, color_team_2.color_positions)
        
        frame = Tracer.draw_car_skeleton(frame, x)

        # display cam
        cv2.imshow('Webcam', frame)
        
        # filter = cv2.bitwise_and(frame, frame, mask=team_A_filter.mask)
        # cv2.imshow('masked', filter)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit

    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
