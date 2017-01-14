import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

actornames_to_ratings = {}
df = pd.read_csv('movie_metadata.csv')  # dataframe

for i in range(0, len(df)):
    for x in (df['actor_1_name'], df['actor_2_name'], df['actor_3_name']):
        name = x[i]
        if pd.notnull(name) and not name.isspace():
            if name in actornames_to_ratings:
                actornames_to_ratings[name].append(float(df['imdb_score'][i]))
            else:
                actornames_to_ratings[name] = [float(df['imdb_score'][i])]
top_rated_actors = []
top_rated_actors_max_rating = []
top_rated_actors_min_rating = []
top_rated_actors_rating = []
for name in sorted(actornames_to_ratings, key=lambda k: np.mean(actornames_to_ratings[k]), reverse=True):
    if len(actornames_to_ratings[name]) > 8:
        top_rated_actors_min_rating.append(min(actornames_to_ratings[name]))
        top_rated_actors_max_rating.append(max(actornames_to_ratings[name]))
        top_rated_actors.append(name)
        top_rated_actors_rating.append(np.mean(actornames_to_ratings[name]))

f = plt.figure()
f.suptitle('Top actors based on average IMDB ratings')
f.canvas.set_window_title('fig_2_top_actors_average_ratings')
plt.plot(list(reversed(top_rated_actors_rating[:30])),
         range(1, 31),
         'o',
         color='blue',
         alpha=0.5,
         markersize=8)
# plt.hlines(range(1, 31),
#            list(reversed(top_rated_actors_min_rating[:30])),
#            list(reversed(top_rated_actors_max_rating[:30])),
#            color='blue',
#            alpha=0.5)
plt.yticks(range(1, 31), list(reversed(top_rated_actors[:30])))

print actornames_to_ratings['Leonardo DiCaprio']

# add a 'best fit' line
plt.xlabel('Average IMDB Rating')
plt.ylabel('Actor name')
plt.gcf().subplots_adjust(left=0.3)
plt.ylim([0, 31])
plt.xticks(np.arange(6.9, 8.1, 0.1))
plt.grid(True)
plt.show()
