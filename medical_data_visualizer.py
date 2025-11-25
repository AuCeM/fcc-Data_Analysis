import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
BMI = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = np.where(BMI < 25, 0, 1)

# 3
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable']).value_counts().sort_index().reset_index()
    df_cat.rename(mapper={'value': 'total'}, axis=1, inplace=True)

    # 7
    # 8
    my_catplot = sns.catplot(data=df_cat,
                      kind='bar',
                      x='variable',
                      y='count',
                      col='cardio',
                      hue='total')

    # 9
    fig = my_catplot.fig
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
                & (df['height'] >= df['height'].quantile(0.025))
                & (df['height'] <= df['height'].quantile(0.975))
                & (df['weight'] >= df['weight'].quantile(0.025))
                & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    lower_corr = corr.mask(mask)

    # 14
    fig, ax = plt.subplots(figsize=(10, 6))

    # 15
    sns.heatmap(lower_corr,
                vmin=-0.16,
                vmax=0.28,
                center=0,
                annot=True,
                fmt=".1f",
                linewidths=0.7,
                ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
