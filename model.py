import pandas as pd
import os

DATASETS_PATH = "C:/Users/Amir/technolab"
df_recommend = pd.read_csv(os.path.join(DATASETS_PATH, 'cluster_recommend_dataset.csv'))

def recommend_me_by_track(x, n = 1):
    if x in list(df_recommend["track_name"]):
        c_df = df_recommend[df_recommend["track_name"] == x][["cluster", "popularity"]]
        c_df.sort_values("popularity", ascending = False, inplace=True)
        c_no = int(c_df["cluster"][0:1])
        r_df = df_recommend[df_recommend["cluster"] == c_no][["track_name", "artist_name", "album_name", "popularity"]]
        r_df.sort_values("popularity", ascending = False, inplace=True)
        n=int(n)
        r_df.reset_index(drop=True, inplace=True)
        result = r_df.iloc[1:n+1, 0:3]

        return result
    else:
        return "Our database has no track with this name"