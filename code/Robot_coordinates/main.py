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
    color_team_1 = Color(np.array(Team1.LOWER_VAL.value), np.array(Team1.UPPER_VAL.value), Team1.FRONT_COLOR.value)
    color_team_2 = Color(np.array(Team2.LOWER_VAL.value), np.array(Team2.UPPER_VAL.value), Team2.FRONT_COLOR.value)

    all_colors_list = [
        color_team_1, 
        color_team_2, 
        ]

    # Set all of the robots
    team_1_striker_1 = car()
    team_1_striker_2 = car()
    team_1_goalie = car()
    team_2_striker_1 = car()
    team_2_striker_2 = car()
    team_2_goalie = car()

    all_robots_list = [
        team_1_striker_1, 
        team_1_striker_2,
        team_1_goalie,
        team_2_striker_1,
        team_2_striker_2,
        team_2_goalie
    ]

    # for each frame
    while True:

        # read webcam
        ret, frame = cam.read() 
        # all_masks = 0
        for color in all_colors_list:
            # apply the mask filter color on the frame
            color.create_mask(frame)

            # all_masks += color.mask

            # get and set coordinates of all found objects
            color.contours = Tracer.get_contours(color.mask)

            # get the center point of every contour
            color.color_positions = Tracer.get_contours_center_point(color.contours)

        team_1_striker_1.coordinates = Tracer.compare_distance_center_points(color_team_1.color_positions, color_team_2.color_positions)
        
        frame = Tracer.draw_car_skeleton(frame, team_1_striker_1.coordinates)

        # display cam
        cv2.imshow('Webcam', frame)
        # filter = cv2.bitwise_and(frame, frame, mask=all_masks)
        # cv2.imshow('masked', filter)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit

    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
