"""This module contains a collection of functions to visualize water level data."""

import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """The function returns a plot of the water level data against time for a station, 
    and include on the plot lines for the typical low and high levels. """

    # Draw high and low range
    if station.typical_range != None:
        plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '--')
        plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '--')

    # Plot
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """The function returns a plot of the water level data against time for a station, 
    including the best fit line of the data."""

    func, shift = polyfit(dates, levels, p)

    float_dates = matplotlib.dates.date2num(dates)

    # Draw high and low range
    if station.typical_range != None:
        plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '--')
        plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '--')

    # Plot the real data
    plt.plot(dates, levels)

    # Plot the best-fit (with 50 points throughout the interval)
    x = np.linspace(float_dates[0],float_dates[-1],50)
    plt.plot(x, func(x - shift))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()