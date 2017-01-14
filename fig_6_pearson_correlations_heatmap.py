import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import seaborn as sns

df = pd.read_csv('movie_metadata.csv')  # dataframe
df = df.sort_index(axis=1)
print df.info()

# Change 'color' column to int based
for i in range(0, len(df['color'])):
    if pd.notnull(df['color'][i]):
        if df['color'][i].lower() == 'color':
            df.loc[i, 'color'] = 1
        elif 'black' in df['color'][i].lower():
            df.loc[i, 'color'] = 0
        else:
            print "something."
df.color = df.color.astype(float)

df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna().astype(np.float32)

corr = df.corr(method='pearson')
print corr['imdb_score'].sort_values(ascending=False)


plt.figure(figsize=(7, 7))
sns.heatmap(corr, vmax=1, square=True)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.gcf().subplots_adjust(left=0.2)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()
