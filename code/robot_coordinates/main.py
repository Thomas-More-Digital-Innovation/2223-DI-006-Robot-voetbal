import cv2
from var import Blue, Pink, Orange
from roboCarTracer import Color, Car, Ball


def main():
    '''
    Write your code here.
    '''
    cv2.destroyAllWindows()


if __name__ == '__main__':

    '''
    Here, you should make sure you capture the right input devide or footage.
    More information on capturing the right device: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a5d5f5dacb77bbebdcbfb341e3d4355c1
    Also make sure you set a resolution that fits the video resolution.
    '''

    # start capturing the webcam
    cam = cv2.VideoCapture(0) 

    # set capturing resolution
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    main()
