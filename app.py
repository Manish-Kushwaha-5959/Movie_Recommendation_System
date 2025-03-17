import streamlit as st
import pandas as pd
import requests
import pickle

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d503008795377effc30c0fe86fda10c4&language=en-US'.format(movie_id))
    file = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + file['poster_path']

def recommend(movie):
    idx = movie_data.title[movie_data.title == movie].index[0]
    distance = movie_model.loc[idx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key= lambda x:x[1])[1:7]
    movie_list_idx = []
    for j in movie_list:
        movie_list_idx.append(j[0])
    ans = []
    poster_path = []
    for k in movie_list_idx:
        movie_id = movie_data.movie_id[k]
        ans.append(movie_data.title[k])
        poster_path.append(fetch_poster(movie_id))
    return ans, poster_path

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
model_dict = pickle.load(open('model_dict.pkl', 'rb'))

movie_data = pd.DataFrame(movie_dict)
movie_model = pd.DataFrame(model_dict)

st.title("Movie Recommendation System")

movie_name = st.selectbox(
    "Enter Movie Name : ",
    movie_data["title"]
)

if st.button("Recommend"):
    name, poster = recommend(movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(poster[0])
        st.text(name[0])
    with col2:
        st.image(poster[1])
        st.text(name[1])
    with col3:
        st.image(poster[2])
        st.text(name[2])
    with col1:
        st.image(poster[3])
        st.text(name[3])
    with col2:
        st.image(poster[4])
        st.text(name[4])
    with col3:
        st.image(poster[5])
        st.text(name[5])