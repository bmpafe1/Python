import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/00b3a987e78548cd5c91e8196aac0120b908e48e/epa-sea-level.csv")

    # Create scatter plot
    new_df = df.drop(['Lower Error Bound','Upper Error Bound','NOAA Adjusted Sea Level'], axis=1)
    x = new_df['Year']
    y = new_df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, color = 'blue',label='Data points')
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y) 
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, color='red', label='Fit: 1880-2013')
    
    # Create second line of best fit
    new_df_2000 = new_df[new_df['Year'] >= 2000]
    x_2000 = new_df_2000['Year']
    y_2000 = new_df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = stats.linregress(x_2000, y_2000)
    y_pred_2000 = slope_2000 * x_pred + intercept_2000
    plt.plot(x_pred, y_pred_2000, color='green', label='Fit: 2000-2013')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()