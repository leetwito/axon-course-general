import numpy as np
import cv2
import imageio
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt


import scipy
from scipy import sparse
import skimage
from skimage import measure

FILE_NAME = 'video.avi'
N_FRAMES_FOR_BACKGROUND = 30
THRESHOLD = 0.14
KERNEL_SIZE = (7, 7)
KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, KERNEL_SIZE) # shapes: [0,1,2] = [rect,cross,elipse]
MAX_SIZE = 10
CENTER_N = 1920/2
CENTER_M = 1080/2

# cap = cv2.VideoCapture()
vid = imageio.get_reader(FILE_NAME)
background_vid = []
print("starting")

for i in range(N_FRAMES_FOR_BACKGROUND):
    # frame = cap.read()
    frame = vid.get_data(i)
    frame = matplotlib.colors.rgb_to_hsv(frame)
    background_vid.append(frame)
    # if i == 3:
    #     cv2.imshow('third frame', frame)
    #     cv2.waitKey(0)

background_frame = np.median(background_vid, axis=0)
# print background_vid
# print background_frame.shape
# cv2.imshow('background_frame', background_frame)
# cv2.waitKey(0)

while i < 70:
    frame = vid.get_data(i)
    frame = matplotlib.colors.rgb_to_hsv(frame)
    dist_frame = background_frame - frame
    thresholded_frame  = np.sqrt(dist_frame[:, :, 0] ** 2 + dist_frame[:, :, 1] ** 2)
    thresholded_frame[thresholded_frame < THRESHOLD] = 0 # background
    thresholded_frame[thresholded_frame >= THRESHOLD] = 1 # object
    # cv2.imshow('thresholded_frame', thresholded_frame)
    # cv2.waitKey(0)
    filtered_binary = cv2.dilate(cv2.erode(thresholded_frame, KERNEL), KERNEL)  # getStructuringElement for kernel
    filtered_binary = cv2.erode(cv2.dilate(filtered_binary, KERNEL), KERNEL)
    filtered_binary[CENTER_M, CENTER_N] = 1
    cv2.imshow('output', filtered_binary)
    cv2.waitKey(0)
    print i
    i = i + 1
    # cv2.imshow('frame', frame)
    # cv2.waitKey(0)

    # all_labels = measure.label(filtered_binary) * 160
    # cv2.imshow('output2', all_labels)
    # cv2.waitKey(0)

    # segment_label = all_labels[CENTER_M, CENTER_N]
    # if segment_label == 0:
    #     continue

    # all_labels[all_labels == segment_label] = 1 # object
    # all_labels[all_labels != segment_label] = 0 # background
    # cv2.imshow('output2', all_labels)
    # cv2.waitKey(0)

    # all_labels3 = np.array([all_labels, all_labels, all_labels])
    blurred_frame = cv2.filter2D(frame, -1, KERNEL)
    output = np.zeros((1080, 1920, 3))
    # output[:, :, 0] = blurred_frame[:, :, 0]*(1-filtered_binary) + frame[:, :, 0] * filtered_binary
    # output[:, :, 1] = blurred_frame[:, :, 1]*(1-filtered_binary) + frame[:, :, 1] * filtered_binary
    # output[:, :, 2] = blurred_frame[:, :, 2]*(1-filtered_binary) + frame[:, :, 2] * filtered_binary
    output[:, :, 0] = frame[:, :, 0] * filtered_binary
    output[:, :, 1] = frame[:, :, 1] * filtered_binary
    output[:, :, 2] = frame[:, :, 2] * filtered_binary
    output = matplotlib.colors.hsv_to_rgb(output)
    cv2.imshow('output', frame)
    cv2.waitKey(0)
    cv2.imshow('output', output)
    cv2.waitKey(0)
    # break




# plt.imshow(all_labels, cmap='spectral')
# plt.show()

# [n_components, labels] = scipy.sparse.csgraph.connected_components(filtered_binary[0:1080, 0:1080])
# print n_components, labels
# print 'labels shape:{}'.format(labels.shape)



cv2.destroyAllWindows()


