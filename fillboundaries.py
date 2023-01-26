import cv2
import numpy as np
import os
# img =cv2.imread('dataset/training_set/000_HC_Annotation.png')
# cv2.imshow('imfdg',img)
# cv2.waitKey(0)




def fillEllipseContour(imgname):
	img =cv2.imread(trainPath + str(imgname))
	image_copy = img.copy()

	# img_gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

	ret, thresh = cv2.threshold(image_copy, 150, 255, cv2.THRESH_BINARY_INV)
	im_floodfill = thresh.copy()
	h,w = thresh.shape[:2]
	mask = np.zeros((h+2,w+2), np.uint8)

	# fills a connected component starting from the seed point with the specified color.
	# The connectivity is determined by the color/brightness closeness of the neighbor pixels.
	cv2.floodFill(im_floodfill,mask,(0,0), (0,0,0))
	#TODO: check for pixel offsets introduced by countour boundaries and filling
	# cv2.imshow('imfdg',im_floodfill)
	# cv2.waitKey(0)
	cv2.imwrite(trainPath + str(imgname),im_floodfill)




# contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# # cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# cv2.fillPoly(image_copy, pts =contours, color=(255,255,255))

# cv2.imshow('imfdg',im_floodfill)
# cv2.waitKey(0)

trainPath = "dataset_filled/training_set/"
# testPath = "test_set/"
trainList = sorted(os.listdir(trainPath))
# testList = sorted(os.listdir(testPath))


for i, item in enumerate(trainList):
    if i % 2 != 0 and i<=3 :
        fillEllipseContour(item)