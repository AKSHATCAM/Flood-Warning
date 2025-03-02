"""This module contains a collection of functions to visualize water level data."""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """This module is for Task 2E. The function returns a plot of the water level data against time for a station, 
    and include on the plot lines for the typical low and high levels. """
    if station.typical_range != None:
        low = station.typical_range[0]
        high = station.typical_range[1]
        plt.axhline(y = low, color = 'r', linestyle = '--')
        plt.axhline(y = high, color = 'r', linestyle = '--')

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()