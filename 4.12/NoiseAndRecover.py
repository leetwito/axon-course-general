import cv2
import numpy as np

def buildEvMat(A):
    en, ev = np.linalg.eig(A) #eigen-numbers and eigen-vector
    B = []
    # for i in

A = cv2.imread('Lenna.png', 0)
# print type(A)
# print np.size(A,1)
# cv2.imshow('image', A)
# cv2.waitKey(0)

W = A * cv2.transpose(A)

