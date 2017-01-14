import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from sklearn import cross_validation
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LinearRegression

df = pd.read_csv('movie_metadata.csv')  # dataframe

# Mult score by 10 and make it integer
# for i in range(0, len(df['imdb_score'])):
#     df.loc[i, 'imdb_score'] = int(df['imdb_score'][i] * 10)
# df.imdb_score = df.imdb_score.astype(int)

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

df = df.select_dtypes(include=['float64', 'int64', 'int'])
df = df.dropna().astype(np.float32)
# df = df.dropna().astype(np.float32)

# x = df[df.columns.difference(['imdb_score'])]
x = df[['num_voted_users',
        'duration',
        'num_critic_for_reviews',
        'num_user_for_reviews',
        'movie_facebook_likes',
        'gross',
        'director_facebook_likes',
        'color',
        'title_year']]
y = df['imdb_score']

val = 0
for i in range(0, 100):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    regr = LinearRegression()
    # regr = RandomForestClassifier()
    regr.fit(x_train, y_train)
    val += regr.score(x_test, y_test)
print val / 100
