import math
import cv2
import time

def estimateSpeed(location1, location2):
	d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
	ppm = 8 #Pixels per Meter
	d_meters = d_pixels / ppm
	time_constant = 15 * 3.6
	speed = d_meters * time_constant
	return speed

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0]-A[0])

def intersect(A, B, C,D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def fps():
    
    video = cv2.VideoCapture('test1.mp4')
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    num_frames = 120
    print("Capturing {0} frames".format(num_frames))
    start = time.time()
    
    for i in range(0, num_frames) :
        ret, frame = video.read()
 
    # End time
    end = time.time()
 
    # Time elapsed
    seconds = end - start
    print ("Time taken : {0} seconds".format(seconds))
 
    # Calculate frames per second
    fps  = num_frames / seconds
    print("Estimated frames per second : {0}".format(fps))
    video.release()
    return fps
