import streamlit as st
import pandas as pd
from io import StringIO
from importlib.machinery import SourceFileLoader
import requests

rating_count_df  = "https://raw.githubusercontent.com/Veronica-MN/wbsflix_streamlit_app/main/sample_movies.csv"

genres = ['Comedy', 'Drama', 'Thriller']

st.title("Personal Recommender")
st.write("Hi! I'm your personal recommender.")


import streamlit as st
import pandas as pd
#from your_popularity_based_recommender_module import popularity_recommender


def popularity_based_recommender(n):
  movie_info_columns = ['movieId', 'title', 'genres']
  rating_count_df = ratings.groupby('movieId')['rating'].agg(['mean', 'count']).reset_index()
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler(feature_range=(1, 5))
  rating_count_df['scaled_count'] = scaler.fit_transform(rating_count_df[['count']])
  rating_count_df['rank'] = (rating_count_df['mean'])+rating_count_df['scaled_count']

  df= (
   rating_count_df 
   .drop_duplicates(subset='movieId')
   .merge(rating_count_df.drop_duplicates(subset='movieId'),
       on='movieId',
       how='left')
    [movie_info_columns + ["mean", "count", "rank"]]
    .nlargest(10, 'rank')
     )

  return df.head(10)


genres = {'1': 'Comedy', '2': 'Drama', '3': 'Thriller'}

#st.title("Personal Recommender")
#st.chat_message("assistant", "Hi! I'm your personal recommender Human!!!")



genre = st.radio("Choose your genre:", genres)

if genre:
    st.write(f"You have chosen {genre}")
    #df = popularity_recommender(15)
    if genre == 'Comedy':
        a = rating_count_df[rating_count_df ["genres"].str.contains("Comedy")]
    elif genre == 'Drama':
        a = rating_count_df[rating_count_df ["genres"].str.contains("Drama")]
    elif genre == 'Thriller':
        a = rating_count_df [rating_count_df ["genres"].str.contains("Thriller")]
    else:
        st.write("Invalid genre selection")

    #if not a.empty:
        #st.write("Recommended movies:")
        #st.table(a[['title']].reset_index(drop=True))
    #else:
        #st.write("No recommendations found for this genre.")


