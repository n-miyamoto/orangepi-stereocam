import cv2
import numpy as np
import glob

square_size = 2.2      # rect size [cm]
pattern_size = (10, 7)

pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
pattern_points *= square_size
objpoints = []
imgpoints = []
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# path of calibration images
#images = files =glob.glob("./calib_images_left/*.jpg")
images = files =glob.glob("./calib_images_right/*.jpg")

def main():
    # extract corners from chess board images
    for image in images:
        # show filename 
        print(image)

        # load images
        bgr = cv2.imread(image, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

        # find corner from chessboard
        ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

        if ret == True:
            print("corner detected!!!")
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(bgr, pattern_size, corners2,ret)
            cv2.imshow('img',img)
            cv2.waitKey(0)

            imgpoints.append(corners.reshape(-1, 2))
            objpoints.append(pattern_points)

    # calibrate camera parameters
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # save camera parameters
    np.save("mtx", mtx)
    np.save("dist", dist.ravel())

    # show parameters
    print("RMS = ", ret)
    print("mtx = \n", mtx)
    print("dist = ", dist.ravel())

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
