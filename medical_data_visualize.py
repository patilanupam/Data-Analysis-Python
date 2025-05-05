import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load and preprocess
df = pd.read_csv('medical_examination.csv')
df['overweight'] = (df['weight'] / (df['height'] / 100)**2 > 25).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # Melt for categorical plot
    df_cat = df.melt(
        id_vars=['cardio'],
        value_vars=['active','alco','cholesterol','gluc','overweight','smoke']
    )
    g = sns.catplot(
        x='variable', hue='value', col='cardio',
        kind='count', data=df_cat
    )
    g.fig.suptitle("Categorical Plot", y=1.03)
    plt.savefig('catplot.png')
    return g.fig

def draw_heat_map():
    # Clean data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975))) &
        (df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975)))
    ]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", ax=ax)
    fig.suptitle("Heat Map of Medical Features", y=1.02)
    plt.savefig('heatmap.png')
    return fig

if __name__ == '__main__':
    draw_cat_plot()
    draw_heat_map()
