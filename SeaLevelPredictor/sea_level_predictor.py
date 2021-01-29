import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x_ax = df['Year']
    y_ax = df['CSIRO Adjusted Sea Level']
    plt.scatter(x_ax,y_ax, color='orange', alpha=0.75)
    # Create first line of best fit
    regression_calculations = linregress(x_ax, y_ax)
    sl = regression_calculations[0]
    inter = regression_calculations[1]
    
    x_years = np.array(list(range(1880, 2050)))
    y_inches = sl * x_years + inter
    
    plt.plot(x_years, y_inches, 'blue')

    # Create second line of best fit
    x_ax = df.loc[df["Year"] >= 2000]['Year']
    y_ax = df.loc[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]

    regression_calculations2 = linregress(x_ax, y_ax)
    sl2 = regression_calculations2[0]
    inter2 = regression_calculations2[1]
    x_years2 = np.array(list(range(2000, 2050)))
    y_inches2 = sl2 * x_years2 + inter2

    plt.plot(x_years2, y_inches2, 'red')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()