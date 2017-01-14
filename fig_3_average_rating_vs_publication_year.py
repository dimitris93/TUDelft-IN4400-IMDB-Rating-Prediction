import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

df = pd.read_csv('movie_metadata.csv')  # dataframe
year_to_ratings = [None] * 3000
for i in range(0, len(df)):
    if pd.notnull(df['title_year'][i]):
        if year_to_ratings[int(df['title_year'][i])] is None:
            year_to_ratings[int(df['title_year'][i])] = [df['imdb_score'][i]]
        else:
            year_to_ratings[int(df['title_year'][i])].append(df['imdb_score'][i])

years = []
average_ratings = []

for i in range(0, len(year_to_ratings)):
    if year_to_ratings[i] is not None:
        years.append(i)
        average_ratings.append(np.mean(year_to_ratings[i]))

f = plt.figure()
f.suptitle('Average IMDB rating vs publication year of the movie')
f.canvas.set_window_title('fig_3_average_rating_vs_publication_year')
plt.plot(years,
         average_ratings,
         'o',
         color='blue',
         alpha=0.5,
         markersize=7)
plt.plot(years, np.poly1d(np.polyfit(years, average_ratings, 1))(years), color='green', alpha=0.5, linewidth=5)
plt.xlabel('Movie\'s publication year')
plt.ylabel('Average IMDB Rating')
plt.show()
