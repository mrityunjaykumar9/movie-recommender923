import pickle
import streamlit as st
import pandas as pd
import requests


def fetch_poster(m):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(m)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    post_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return post_path


def fetch_language(m):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(m)
    data = requests.get(url)
    data = data.json()
    language = data['original_language']
    return language


def fetch_date(m):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(m)
    data = requests.get(url)
    data = data.json()
    release_date = data['release_date']
    return release_date


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    movie_names = []
    movie_posters = []
    movie_language = []
    movie_date = []

    for i in distances[0:15]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        movie_posters.append(fetch_poster(movie_id))
        movie_names.append(movies.iloc[i[0]].title)
        movie_language.append(fetch_language(movie_id))
        movie_date.append(fetch_date(movie_id))

    return movie_names, movie_posters, movie_language, movie_date


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    movie_names, movie_posters, movie_language, movie_date = recommend(selected_movie)

    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10, col11, col12 = st.columns(4)

    with col1:
        st.markdown(movie_names[0])
        st.image(movie_posters[0])
        st.caption('language : ' + movie_language[0])
        st.caption('release date : ' + movie_date[0])
    with col2:
        st.markdown(movie_names[1])
        st.image(movie_posters[1])
        st.caption('language : ' + movie_language[1])
        st.caption('release date : ' + movie_date[1])
    with col3:
        st.markdown(movie_names[2])
        st.image(movie_posters[2])
        st.caption('language : ' + movie_language[2])
        st.caption('release date : ' + movie_date[2])
    with col4:
        st.markdown(movie_names[3])
        st.image(movie_posters[3])
        st.caption('language : ' + movie_language[3])
        st.caption('release date : ' + movie_date[3])
    with col5:
        st.markdown(movie_names[4])
        st.image(movie_posters[4])
        st.caption('language : ' + movie_language[4])
        st.caption('release date : ' + movie_date[4])
    with col6:
        st.markdown(movie_names[5])
        st.image(movie_posters[5])
        st.caption('language : ' + movie_language[5])
        st.caption('release date : ' + movie_date[5])
    with col7:
        st.markdown(movie_names[6])
        st.image(movie_posters[6])
        st.caption('language : ' + movie_language[6])
        st.caption('release date : ' + movie_date[6])
    with col8:
        st.markdown(movie_names[7])
        st.image(movie_posters[7])
        st.caption('language : ' + movie_language[7])
        st.caption('release date : ' + movie_date[7])
    with col9:
        st.markdown(movie_names[8])
        st.image(movie_posters[8])
        st.caption('language : ' + movie_language[8])
        st.caption('release date : ' + movie_date[8])
    with col10:
        st.markdown(movie_names[9])
        st.image(movie_posters[9])
        st.caption('language : ' + movie_language[9])
        st.caption('release date : ' + movie_date[9])
    with col11:
        st.markdown(movie_names[10])
        st.image(movie_posters[10])
        st.caption('language : ' + movie_language[10])
        st.caption('release date : ' + movie_date[10])
    with col12:
        st.markdown(movie_names[11])
        st.image(movie_posters[11])
        st.caption('language : ' + movie_language[11])
        st.caption('release date : ' + movie_date[11])


