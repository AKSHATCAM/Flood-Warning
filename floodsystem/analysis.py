import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def polyfit(dates, levels, p):
    """Compute the least-squares fit of a polynomial with degree p.
    This function returns a tuple containing polynomial, shift of the time axis"""
    float_dates = matplotlib.dates.data2num(dates)

    # Compute the coefficients of the best-fit polynomial
    coeff = np.polyfit(float_dates - float_dates[0], levels, p)

    # Substituting the coefficients into a one-dimensional polynomial, which can be evaluated afterwards
    func = np.poly1d(coeff)
    return (func, float_dates[0])