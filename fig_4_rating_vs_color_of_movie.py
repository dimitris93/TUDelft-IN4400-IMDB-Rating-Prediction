import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

df = pd.read_csv('movie_metadata.csv')  # dataframe
year_to_ratings = [None] * 3000

color_ratings = []
black_and_white_ratings = []

for i in range(0, len(df)):
    if pd.notnull(df['color'][i]):
        if df['color'][i].lower() == 'color':
            color_ratings.append(df['imdb_score'][i])
        elif 'black' in df['color'][i].lower():
            black_and_white_ratings.append(df['imdb_score'][i])
        else:
            print "something."

f = plt.figure()
f.suptitle('IMDB rating vs color of movie')
f.canvas.set_window_title('fig_4_rating_vs_color_of_movie')
plt.hist(color_ratings,
         bins=np.arange(0, 10 + 0.5, 0.5),
         color='green',
         alpha=0.5,
         normed=True,
         label='Colored')
plt.hist(black_and_white_ratings,
         bins=np.arange(0, 10 + 0.5, 0.5),
         color='black',
         alpha=0.5,
         normed=True,
         label='Black & White')
plt.legend(loc='best')
plt.xticks(range(0, 11))
plt.xlabel('IMDB Rating')
plt.ylabel('Probability')

f = plt.figure()
f.suptitle('IMDB rating vs color of movie')
f.canvas.set_window_title('fig_4_rating_vs_color_of_movie')
plt.boxplot(color_ratings, positions=[2])
plt.boxplot(black_and_white_ratings, positions=[3])
plt.ylabel('IMDB Rating')
axes = plt.gca()
axes.set_xlim([1, 4])
plt.xticks([2, 3], ['Colored', 'Black & White'])
plt.grid(True)
plt.show()
