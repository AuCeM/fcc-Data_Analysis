import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], alpha=0.4, color='b', marker='o')

    # Create first line of best fit
    linreg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_yrs = np.arange(df['Year'].min(), 2051)

    func1 = linreg1.slope * extended_yrs + linreg1.intercept
    ax.plot(extended_yrs, func1, 'red')

    # Create second line of best fit
    linreg2 = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    ext = np.arange(df[df['Year'] >= 2000]['Year'].min(), 2051)
    func2 = linreg2.slope * ext + linreg2.intercept
    ax.plot(ext, func2, 'green')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
