import numpy as np
import matplotlib.pyplot as plt
import math
import ffmpeg

######## 1 get the diagonal of dot product
# A = np.array([[5,6],[7,8]])
# B = np.array([[1,2],[3,4]])
# Z = np.dot(A,B)
# Z_diag = np.diag(Z)

######## 2 add zeros
# vec = np.arange(5)+1
# new_vec = np.zeros(vec.shape[0]*4)
# new_vec[::4] = vec

######## 3 sliding window
# window_size = 3
# a = np.arange(12)
# a_sum = a
# for i in range(window_size-1):
#     a_sum += np.roll(a, -i - 1)
# avg_arr = a_sum/window_size

######## 4 ditance from point p to line (P0[i], P1[i])
# P0[i] first point of line i
# P1[i] second point of line i
# p the point

# P0 = [(1, 1)]
# P1 = [(2, 2)]
# p = (1, 2)
#
# x0 = p[0]
# y0 = p[1]
# for i in range(len(P0)):
#     x1 = P0[i][0]
#     y1 = P0[i][1]
#     x2 = P1[i][0]
#     y2 = P1[i][1]
#     print x0,y0,x1,y1,x2,y2
#     distance = np.abs( (y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1 )  \
#               / np.sqrt( (y2-y1)**2 + (x2-x1)**2 )

######## 5 rank
# a = np.ones((3,4))
# b = np.linalg.matrix_rank(a)

######## 6 most freq val
# a = np.ones((3, 4))
# a[::2, ::2] = 2
# b = np.histogram(a, bins='auto')
# amounts, values = b[0], b[1]
# common_index = np.argmax(amounts)
# common = values[common_index]
# print common

######## 7
# concatenate matrices A1|A2|... so we'll have n x np matrix
# concatenate vector p1 so we'll have np x 1 vector
#                    p2

# M = [[1,2],[3,4]],[[5,6],[7,8]]
# V = [[9,10],[11,12]]
# p = 2
# super_matrix = M[0]
# super_vector = V[0]
#
# for i in range(p-1):
#     super_matrix = np.concatenate((super_matrix, M[i]), 1)
#     super_vector = np.concatenate((super_vector, V[i]), 0)
# print np.dot(super_matrix,super_vector)




######## Matplotlib
# t = np.linspace(1, 10, 1000)
# x = np.array([math.sin(i) + math.sin(100*i) for i in t])
# plt.subplot(1, 2, 1)
# plt.plot(t, x)
# plt.xlabel('t')
# plt.ylabel('x')
# plt.title('x(t)')
#
# x_fft = np.fft.fft(x)
# x_fft = np.fft.fftshift(x_fft)
# t_fft = np.fft.fftfreq(len(x), 1)
# # t_fft = np.linspace(-math.pi/2, math.pi/2, 1000)
# plt.subplot(1, 2, 2)
# plt.plot(t_fft, x_fft)
# plt.xlabel('freq')
# plt.ylabel('x_fft')
# plt.title('x_fft(freq)')
# plt.show()



