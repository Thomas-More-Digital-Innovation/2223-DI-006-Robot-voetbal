import cv2
from numpy import empty
import var

class car:
    def __init__(self, team, player_type, coordinates, angle):
        pass

class Color:
    def __init__(self, lower_val, upper_val, color):
        self.lower_val = lower_val
        self.upper_val = upper_val
        self.color = color
        self.contours = None
        self.color_positions = None
    
    def create_mask(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(hsv, self.lower_val, self.upper_val)


class Tracer:
    def get_contours(mask):
        contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def get_contours_center_point(contours):
        list = []
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    # compute the center of the contour
                    M = cv2.moments(contour)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    list.append((cX, cY))
        return list

    def compare_distance_center_points(points_list_1, points_list_2):
        list = []
        for pos1 in points_list_1:
            for pos2 in points_list_2:
                dis = ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5
                if dis <= 50:
                    list.append((pos1, pos2, dis))

        return list

        #if there is more than one combination, remove the combinations with the highest distance
        while len(list) > 1:
            pass

    def draw_car_skeleton(frame, coordinates):
        if coordinates:
            cv2.line(frame, coordinates[0][0], coordinates[0][1], (255,255,255), 4)
            cv2.circle(frame, coordinates[0][0], 7, (0, 0, 255), -1)
            cv2.circle(frame, coordinates[0][1], 7, (0, 0, 255), -1)
        
        return frame
