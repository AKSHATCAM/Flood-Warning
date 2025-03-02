"""This module contains a collection of functions to visualize water level data."""

import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def plot_water_levels(station, dates, levels):
    """This module is for Task 2E. The function returns a plot of the water level data against time for a station, 
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