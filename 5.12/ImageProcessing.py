import cv2
import numpy as np
import matplotlib.pyplot as plt


im1 = cv2.imread('Lenna.png', 0) / 255.0
im2 = cv2.imread('Cameraman.jpg', 0)
# print im2.shape

cv2.imshow('Lenna', im1)
# cv2.imshow('Lenna', im1)
cv2.imshow('Cameraman', im2)
cv2.waitKey(0)

im1_fft = np.fft.fft2(im1)
im2_fft = np.fft.fft2(im2)

# plt.imshow(-40*np.log(np.abs(np.fft.fftshift(im1_fft))))
# plt.show()

# amp1 = -40*np.log(np.abs(np.fft.fftshift(im1_fft)))
# amp2 = -40*np.log(np.abs(np.fft.fftshift(im2_fft)))
# phase1 = cv2.phase(np.fft.fftshift(im1_fft))
# phase2 = cv2.phase(np.fft.fftshift(im2_fft))
#


amp1, phase1 = cv2.cartToPolar(np.real(np.fft.fftshift(im1_fft)), np.imag(np.fft.fftshift(im1_fft)))
amp2, phase2 = cv2.cartToPolar(np.real(np.fft.fftshift(im2_fft)), np.imag(np.fft.fftshift(im2_fft)))

x, y = cv2.polarToCart(amp1, phase1)
# im_freq = np.zeros((512,512,2))
# im_freq[:,:,0]=x
# im_freq[:,:,1] =y
im_freq = x + 1j*y
im1_space_phase_changed = np.abs(np.fft.ifft2(np.fft.ifftshift(im_freq)))
print im1_space_phase_changed.shape
plt.imshow(im1_space_phase_changed)
plt.show()



# im1_freq_phase_changed,_ = cv2.polarToCart(amp1, phase2)
# im1_space_phase_changed = np.abs(np.fft.ifft2(np.fft.ifftshift(im1_freq_phase_changed)))
# print im1_space_phase_changed.shape
# plt.imshow(im1_space_phase_changed)
# plt.show()

