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
    if pd.notnull(df['gross'][i]) and pd.notnull(df['title_year'][i]):
        if df['gross'][i] != 0 and df['title_year'][i] > 2000:
            gross.append(df['gross'][i] / 1000000)
            ratings.append(df['imdb_score'][i])

f = plt.figure()
f.suptitle('IMDB rating vs movie\'s gross income')
f.canvas.set_window_title('fig_5_rating_vs_movies_gross_income')
plt.plot(gross,
         ratings,
         'o',
         color='blue',
         alpha=0.25)
plt.xlabel('Gross income in millions')
plt.ylabel('IMDB Rating')
plt.plot(gross, np.poly1d(np.polyfit(gross, ratings, 1))(gross),
         color='green', alpha=0.8, linewidth=6)
plt.yticks(range(0,11))
plt.show()
