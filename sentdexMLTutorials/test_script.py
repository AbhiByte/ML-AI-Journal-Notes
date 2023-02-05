import numpy as np
def rSquared(xs, ys, m, b):
    numerator = 1
    denominator = 0
    rS = numerator/denominator
    return rS
    
def BestFitSlopeAndIntercept(xs, ys):
    numerator = (np.mean(xs) * np.mean(ys)) - (np.mean(xs * ys))
    denominator = np.mean(xs)**2 - np.mean(xs**2)
    m = numerator/denominator

    b = np.mean(ys) - m * np.mean(xs)
    return m, b



xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)
ys = np.array([1, 3, 2, 5, 2, 6, 6, 7, 3, 8], dtype=np.float64)
m, b = BestFitSlopeAndIntercept(xs, ys)
print(rSquared(xs, ys, m , b))
