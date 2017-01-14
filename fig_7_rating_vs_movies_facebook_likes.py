import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

df = pd.read_csv('movie_metadata.csv')  # dataframe
year_to_ratings = [None] * 3000

gross = []
ratings = []

for i in range(0, len(df)):
    if pd.notnull(df['movie_facebook_likes'][i]) and pd.notnull(df['title_year'][i]):
        if df['movie_facebook_likes'][i] != 0 and df['title_year'][i] > 2000:
            gross.append(df['movie_facebook_likes'][i])
            ratings.append(df['imdb_score'][i])

f = plt.figure()
f.suptitle('IMDB rating vs movie\'s Facebook Likes')
f.canvas.set_window_title('fig_7_rating_vs_movies_facebook_likes')
plt.plot(gross,
         ratings,
         'o',
         color='blue',
         alpha=0.25)
plt.xlabel('Facebook Likes of movie')
plt.ylabel('IMDB Rating')
plt.plot(gross, np.poly1d(np.polyfit(gross, ratings, 1))(gross),
         color='green', alpha=0.8, linewidth=5)
plt.yticks(range(0, 11))
plt.xticks(range(0, 400000, 50000), ['0', '50k', '100k', '150k', '200k', '250k', '300k', '350k'])
plt.ylim([0, 10])
plt.show()
