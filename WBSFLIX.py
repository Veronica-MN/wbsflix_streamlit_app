import streamlit as st
import pandas as pd
from io import StringIO
from importlib.machinery import SourceFileLoader

genres = ['Comedy', 'Drama', 'Thriller']

st.title("Personal Recommender")
st.write("Hi! I'm your personal recommender.")


genre = st.radio("Choose your genre:", genres)

if genre:
    st.write(f"You have chosen {genre}")
    df = popularity_recommender(15)
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


# chat bot
import streamlit as st
import pandas as pd
from your_popularity_based_recommender_module import popularity_recommender

genres = {'1': 'Comedy', '2': 'Drama', '3': 'Thriller'}

st.title("Personal Recommender")
st.chat_message("assistant", "Hi! I'm your personal recommender Human!!!")

while True:
    st.chat_message("assistant", "Please choose a movie genre:")
    genre_choice = st.text_input("Choose, 1 = Comedy, 2 = Drama, 3 = Thriller")

    if genre_choice not in genres:
        st.chat_message("assistant", "Invalid genre selection. Please choose 1, 2, or 3.")
    else:
        selected_genre = genres[genre_choice]
        st.chat_message("user", f"You have chosen {selected_genre}")
        df = popularity_recommender(10) 


        a = df[df["genres"].str.contains(selected_genre)] 

        if not a.empty:
            st.chat_message("assistant", "Here is your personal movie recomendations, Enjoy!:")
            for movie_title in a['title']:
                st.chat_message("assistant", movie_title)
        else:
            st.chat_message("assistant", "No recommendations found now, sorry.")

    continue_chat = st.radio("Do you want another recomendation?", ["Yes", "No"])
    if continue_chat == "No":
        break