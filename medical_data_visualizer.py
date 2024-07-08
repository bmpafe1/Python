import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data
df = pd.read_csv('medical_examination.csv')

# 2. Create the overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot
def draw_cat_plot():
    # 5. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat the data
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # 7. Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar',
        height=5,
        aspect=1.2
    ).fig

    # 8. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 10. Draw the Heat Map
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15. Draw the heatmap
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt='.1f', 
        cmap='coolwarm', 
        center=0, 
        square=True, 
        linewidths=.5, 
        cbar_kws={'shrink': .5}
    )

    # 16. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

# Call the functions to draw the plots
draw_cat_plot()
draw_heat_map()
