import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    df=pd.read_csv("https://raw.githubusercontent.com/Bilalkhan-cel/boilerplate-sea-level-predictor/refs/heads/main/epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    years=df['Year']
    sea_level=df['CSIRO Adjusted Sea Level']
    res=linregress(years,sea_level)
    fut_years=np.array(range(1880,2051))
    plt.scatter(years,sea_level)
    plt.plot(fut_years,fut_years*res.slope+res.intercept)


    # Create second line of best fit
    yer=ndf['Year']
    inc=ndf['NOAA Adjusted Sea Level']
    res=linregress(yer,inc)
    fut_years=np.array(range(2000,2051))
    plt.scatter(yer,inc)
    plt.plot(fut_years,fut_years*res.slope+res.intercept)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()