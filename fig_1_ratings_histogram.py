import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

df = pd.read_csv('movie_metadata.csv')  # dataframe

f = plt.figure()
f.suptitle('Distribution of IMDB ratings')
f.canvas.set_window_title('fig_1_ratings_histogram')
(mu, sigma) = norm.fit(df['imdb_score'])
n, bins, patches = plt.hist(df['imdb_score'],
                            bins=40,
                            color='blue',
                            alpha=0.5,
                            normed=True)
plt.plot(bins, mlab.normpdf(bins, mu, sigma), 'r--', color='orange', linewidth=4)
plt.xlabel('IMDB Rating')
plt.ylabel('Probability')

plt.show()
