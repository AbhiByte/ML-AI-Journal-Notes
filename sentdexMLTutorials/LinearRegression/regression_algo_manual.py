#continue from vid1
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Simple sample data
xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)
ys = np.array([1, 3, 2, 5, 2, 6, 6, 7, 3, 8], dtype=np.float64)

def BestFitSlopeAndIntercept(xs, ys):
    numerator = (np.mean(xs) * np.mean(ys)) - (np.mean(xs * ys))
    denominator = np.mean(xs)**2 - np.mean(xs**2)
    m = numerator/denominator

    b = np.mean(ys) - m * np.mean(xs)
    return m, b
def squaredError(ys_orig, ys_line):
    rS = sum((ys_orig - ys_line)**2)
    return rS

def coefOfDet(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_err_reg_line = squaredError(ys_orig, ys_line)
    squared_error_y_mean = squaredError(ys_orig, y_mean_line)
    return 1 - (squared_err_reg_line/squared_error_y_mean)




m, b = BestFitSlopeAndIntercept(xs, ys)
regression_line = [m*x+b for x in xs]

predict_x = 15
predict_y = m*predict_x+b
r_squared = coefOfDet(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.scatter(predict_x, predict_y, color="green")
plt.show()

