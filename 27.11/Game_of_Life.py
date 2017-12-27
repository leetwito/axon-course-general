import numpy as np
import matplotlib.pyplot as plt

def getNeighborsIndices(p, x_max, y_max):
    x = p[0]
    y = p[1]
    neighbors = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
    i = 0
    print neighbors
    for point in neighbors:
        if point[0]>x_max or point[0]<0 or point[1]>y_max or point[1]<0:
            print point
            neighbors.pop(i)
        else:
            i += 1
    return neighbors

def getNumberOfNeighborsAlive(A, p):
    height, width = np.size(A,0), np.size(A,1)
    indices = getNeighborsIndices(p, height-1, width-1) # x_max is 1 less than the height [pyhton's 0 indexing]
    counter = 0
    for i in indices:
        if A[i] == 1:
            counter += 1
    return counter

def nextGenState(A, p):
    if A[p] == 0: # dead cell
        pass

def life(A):
    pass




def main():
    A = np.array([[1,1,1,1],[1,1,1,1],[1,0,1,0],[0,1,0,1]])
    plt.imshow(A)
    plt.show()

if __name__== "__main__":
    # main()

    print getNeighborsIndices((1,4), x_max=4, y_max=4)