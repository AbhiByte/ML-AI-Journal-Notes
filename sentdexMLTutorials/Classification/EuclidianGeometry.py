from math import sqrt

def EuclideanDistance(point1, point2):
    dist = 0
    if len(point1) != len(point1):
        raise ValueError("Point dimensions not equivalent!")
    for i in range(len(point1)):
        dist += (point1[i] - point2[i])**2
    
    return sqrt(dist)
    
    #Can also be done with np arrays
    '''
    return np.linalg.norm(np.array(point1) - np.array(point2))
    '''




if __name__ == '__main__':
    p1 = [1, 3, 25]
    p2 = [2, 5, 6.3]
    print(EuclideanDistance(p1, p2))


    
