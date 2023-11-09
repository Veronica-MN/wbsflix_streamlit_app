# -*- coding: utf-8 -*-
"""popularitywithchatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
https://colab.research.google.com/drive/1N3vjoyz48pKF8s55zcvwT0VVP7fUVCXz
"""

import streamlit as st
import pandas as pd
#from your_popularity_based_recommender_module import popularity_recommender
import numpy as np

# Define the URL for the CSV data
csv_url = "https://raw.githubusercontent.com/Veronica-MN/wbsflix_streamlit_app/main/sample_movies.csv"

# Define the popularity recommender function
def popularity_recommender(num_recommendations):
    try:
        movie_data = pd.read_csv(csv_url)
        movie_data['rating'] = calculate_popularity(movie_data)
        sorted_movies = movie_data.sort_values(by='rating', ascending=False)
        recommended_movies = sorted_movies.head(num_recommendations)
        return recommended_movies
    except Exception as e:
        print(f"Error: {e}")
        return None

# Calculate movie popularity score
def calculate_popularity(movie_data):
    average_ratings = movie_data.groupby('movieId')['rating'].mean()
    popularity_score = (average_ratings * np.log1p(movie_data['rating'].count())).fillna(0)
    return popularity_score

# Define genres and Streamlit title
genres = {'1': 'Comedy', '2': 'Drama', '3': 'Thriller'}

st.title("Personal Recommender")
#st.chat_message("assistant", "Hi! I'm your personal recommender Human!!!")

while True:
    st.chat_message("assistant", "Please choose a movie genre:")
    genre_choice = st.text_input("Choose, 1 = Comedy, 2 = Drama, 3 = Thriller")

    if genre_choice not in genres:
        st.chat_message("assistant", "Invalid genre selection. Please choose 1, 2, or 3.")
    else:
        selected_genre = genres[genre_choice]
        st.chat_message("user", f"You have chosen {selected_genre}")

        recommended_movies = popularity_recommender(10)

        a = recommended_movies[recommended_movies["genres"].str.contains(selected_genre)]

        if not a.empty:
            st.chat_message("assistant", "Here are your personal movie recommendations, Enjoy!:")
            for movie_title in a['title']:
                st.chat_message("assistant", movie_title)
        else:
            st.chat_message("assistant", "No recommendations found now, sorry.")

    continue_chat = st.radio("Do you want another recommendation?", ["Yes", "No"])
    if continue_chat == "No":
        break
