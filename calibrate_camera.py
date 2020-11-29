import cv2
import numpy as np
import glob

images = files =glob.glob("./calib_images")

def main():
    for image in images:
    bgr = cv2.imread(fname, cv2.IMREAD_COLOR)
    #TODO


if __name__ == '__main__':
    main()