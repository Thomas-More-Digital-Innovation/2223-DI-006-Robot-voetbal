from enum import Enum

class TracingParams(Enum):
    MIN_AREA_COLOR = 500
    MAX_DISTANCE_BETWEEN_COLORS = 1000

    
class Blue(Enum):
    LOWER_VAL = [90, 100, 50]
    UPPER_VAL = [150, 255, 255]


class Pink(Enum):
    LOWER_VAL = [160, 50, 50]
    UPPER_VAL = [200, 255, 255]


class Orange(Enum):
    LOWER_VAL = [0, 180, 50]
    UPPER_VAL = [15, 255, 255]
