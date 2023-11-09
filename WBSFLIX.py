import streamlit as st
import pandas as pd
from io import StringIO



uploaded_file = st.file_uploader("top_movies.csv")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe) 



st.title("Personal Recommender")
st.write("Hi! I'm your personal recommender.")

@st.cache_data
uploaded_files = st.file_uploader("top_movies.csv", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("top_movies:", uploaded_file.name)
    st.write(bytes_data)


def popularity_based_recommender(n):
  movie_info_columns = ['movieId', 'title', 'genres']
  rating_count_df = top_movies.groupby('movieId')['rating'].agg(['mean', 'count']).reset_index()
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler(feature_range=(1, 5))
  rating_count_df['scaled_count'] = scaler.fit_transform(rating_count_df[['count']])
  rating_count_df['rank'] = (rating_count_df['mean'])+rating_count_df['scaled_count']

  df= (
   rating_count_df
   .drop_duplicates(subset='movieId')
   .merge(top_movies.drop_duplicates(subset='movieId'),
       on='movieId',
       how='left')
    [movie_info_columns + ["mean", "count", "rank"]]
    .nlargest(10, 'rank')
     )

  return df.head(10)

genre = st.radio("Choose your genre:", genres)

if genre:
    st.write(f"You have chosen {genre}")
    df = popularity_based_recommender(15) 
    if genre == 'Comedy':
        a = df[df["genres"].str.contains("Comedy")]
    elif genre == 'Drama':
        a = df[df["genres"].str.contains("Drama")]
    elif genre == 'Thriller':
        a = df[df["genres"].str.contains("Thriller")]
    else:
        st.write("Invalid genre selection")

    if not a.empty:
        st.write("Recommended movies:")
        st.table(a[['title']].reset_index(drop=True))
    else:
        st.write("No recommendations found for this genre.")



