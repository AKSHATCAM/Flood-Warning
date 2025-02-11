import numpy as np

def trapezium_numintegration(a, b, w):
    """
    Trapezium rule for numerical integration
    f: function to integrate
    a: lower limit
    b: upper limit
    w: weioht of each trapezium (step size) """

    Area = 0.0
    for i in np.arange(a, b, w):
        Area += (f(i) + f(i+w)) * (w/2)
    return Area

def f(x):
    return x**2 + x**3



ACTUAL_aNS = 2833.33333333
ERROR = print("Error: ", (abs(ACTUAL_aNS - trapezium_numintegration(0, 10, 0.5))/ACTUAL_aNS)*100, "%")


