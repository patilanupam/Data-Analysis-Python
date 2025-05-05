import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df['value'], color='tab:blue')
    ax.set_title('Daily freeCodeCamp Forum Page Views')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Prepare monthly data
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = grouped.plot.bar(figsize=(12,8)).figure
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.legend(title='Month')
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy().reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    
    fig, axes = plt.subplots(1, 2, figsize=(14,6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set_title('Year-wise Box Plot')
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1]).set_title('Month-wise Box Plot')
    plt.savefig('box_plot.png')
    return fig

if __name__ == '__main__':
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
