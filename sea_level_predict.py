import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

def draw_sea_level_plot():
    # Scatter
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=20)

    # Regression on all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(df['Year'],
            res_all.intercept + res_all.slope * df['Year'],
            'r', label='Fit: All years')

    # Regression from 2000 onward
    recent = df[df['Year'] >= 2000]
    res_recent = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    ax.plot(recent['Year'],
            res_recent.intercept + res_recent.slope * recent['Year'],
            'g', label='Fit: 2000+')

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    plt.savefig('sea_level_plot.png')
    return fig

if __name__ == '__main__':
    draw_sea_level_plot()
