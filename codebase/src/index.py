import pandas as pd
songs_data = '../data/data.csv'
songs_df = pd.read_csv(songs_data)
songs = songs_df.to_dict('records')

print(songs[0])