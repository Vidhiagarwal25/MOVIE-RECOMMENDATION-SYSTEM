import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movie = []
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

movie_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity =pickle.load(open('similarity.pkl','rb'))

st.title('what you should watch today')
selected_movie = st.selectbox(
'movies',
movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)
