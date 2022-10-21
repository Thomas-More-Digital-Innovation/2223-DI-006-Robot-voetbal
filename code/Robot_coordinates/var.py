from enum import Enum

class TracingParams(Enum):
    MIN_AREA_COLOR = 700
    MAX_DISTANCE_BETWEEN_COLORS = 1000

class Team1(Enum):
    LOWER_VAL = [90, 100, 50]
    UPPER_VAL = [130, 255, 255]
    COLOR_STRING = 'blue'


class Team2(Enum):
    LOWER_VAL = [160, 50, 50]
    UPPER_VAL = [200, 255, 255]
    COLOR_STRING = 'pink'


class PlayerOffenceOne(Enum):
    LOWER_VAL = [0, 125, 0]
    UPPER_VAL = [30, 255, 255]
    COLOR_STRING = 'yellow'


class PlayerOffenceTwo(Enum):
    LOWER_VAL = None
    UPPER_VAL = None
    COLOR_STRING = 'Brown'


class PlayerDefence(Enum):
    LOWER_VAL = None
    UPPER_VAL = None
    COLOR_STRING = 'purple'


class Ball(Enum):
    LOWER_VAL = [0, 180, 50]
    UPPER_VAL = [15, 255, 255]
    COLOR_STRING = 'orange'