import math
import cv2
import numpy as np
from typing import Tuple
from var import TracingParams

def get_contours_center_point(mask:np.ndarray) -> list:
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    list = []
    if len(contours) != 0:
        for contour in contours:
                if cv2.contourArea(contour) > TracingParams.MIN_AREA_COLOR.value:
                    # compute the center of the contour
                    M = cv2.moments(contour)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    list.append((cX, cY))
    return list

def compare_distance_center_points(position_list_1:list, position_list_2:list) -> list:
    list = ((0,0), (0,0), TracingParams.MAX_DISTANCE_BETWEEN_COLORS.value)
    for pos1 in position_list_1:
        for pos2 in position_list_2:
            dis = ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5
            if dis <= TracingParams.MAX_DISTANCE_BETWEEN_COLORS.value:
                #if there is more than one combination, remove the combinations with the highest distance
                if dis < list[2]:
                    list = (pos1, pos2, dis)

    return list

def get_coord_and_angle(coordinates:tuple) -> Tuple[tuple, float]:
    point_1_x = coordinates[0][0]
    point_1_y = coordinates[0][1]
    point_2_x = coordinates[1][0]
    point_2_y = coordinates[1][1]
    
    angle = math.degrees(math.atan2(point_1_y - point_2_y, point_1_x - point_2_x)) % 360
    center_coord = (int(point_1_x+(point_2_x-point_1_x)/2), int(point_1_y+(point_2_y-point_1_y)/2))

    return center_coord, angle


class Color:
    def __init__(self, lower_val:list, upper_val:list) -> None:
        self.lower_val = np.array(lower_val)
        self.upper_val = np.array(upper_val)

    def create_mask(self, frame: np.ndarray) -> None:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(hsv, self.lower_val, self.upper_val)
    

class Car:
    def __init__(self, color_1:Color, color_2:Color) -> None:
        self.color_1 = color_1
        self.color_2 = color_2
    
    def get_coordinate_angle(self, frame:np.ndarray) -> Tuple[tuple, float]:
        self.color_1.create_mask(frame)
        self.color_2.create_mask(frame)
        contour_center_1 = get_contours_center_point(self.color_1.mask)
        contour_center_2 = get_contours_center_point(self.color_2.mask)
        self.distance_between = compare_distance_center_points(contour_center_1, contour_center_2)
        self.coord, self.angle = get_coord_and_angle(self.distance_between)

        return self.coord, self.angle

    def draw(self, frame:np.ndarray) -> np.ndarray:
        if self.distance_between:
            cv2.line(frame, self.distance_between[0], self.distance_between[1], (255,255,255), 2)
            cv2.circle(frame, self.distance_between[0], 5, (255, 255, 0), -1)
            cv2.circle(frame, self.distance_between[1], 5, (0, 0, 255), -1)
            cv2.circle(frame, self.coord, 5, (255, 255, 255), -1)
        
        return frame


class Ball:
    def __init__(self, color:Color) -> None:
        self.color = color

    def get_coordinate(self, frame:np.ndarray):
        self.color.create_mask(frame)
        self.coord = get_contours_center_point(self.color.mask)

        return self.coord
    
    def draw(self, frame:np.ndarray) -> np.ndarray:
        if self.coord:
            cv2.circle(frame, self.coord[0], 5, (0, 255, 0), -1)
        
        return frame
