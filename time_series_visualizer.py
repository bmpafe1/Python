import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/10d2fe8058be34cdf47d730d03e5ee1500bf23cf/fcc-forum-pageviews.csv")
#Set the index to the date column.
#df = df.set_index('date')
#filtering out days
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
#Create a draw_line_plot function
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(20, 5))
    df_line = sns.lineplot(data=df, x="date", y="value",ax=ax)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# Create draw_bar_plot funtion
def draw_bar_plot():
    fig, ax = plt.subplots(figsize=(20, 5))
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month_name()
    df['year'] = df['date'].dt.year
    ndf = df.drop(['date'],axis=1)
    df_bar = pd.pivot_table(df, values='value', index=['month', 'year'], aggfunc="mean")
    
    # Draw bar plot
    sns.barplot(x = 'year',y = 'value',hue = 'month',data = df_bar)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc='upper left')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
#Create draw_box_plot function
def draw_box_plot():
    df['date'] = pd.to_datetime(df['date'])
    
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.drop(['date'],axis=1)
    
    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(ncols=2)
    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
    df_box=df_box.loc[(df_box['year'] == 2019)]
    sns.boxplot(x='month', y='value', data=df_box, ax=axs[1])
    axs[0].set_ylabel("Page Views", labelpad=25, fontsize=18)
    axs[0].set_xlabel("Year", labelpad=25, fontsize=18)
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].figure.set_size_inches(14, 7)
    axs[1].set_ylabel("Page Views", labelpad=25, fontsize=18)
    axs[1].set_xlabel("Month", labelpad=25, fontsize=18)
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].figure.set_size_inches(14, 7)



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig