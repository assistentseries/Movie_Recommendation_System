import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3c20ff12cb9a6063d3c0553670e58789&language=en-US'.format(movie_id),timeout=10)

    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.markdown(
    """
    <h1 style='color: #4FC3F7; font-size: 40px; font-weight: 700;
               margin-top: 10px; margin-bottom: 25px;'>
        🎬 Movie Recommender System
    </h1>
    """,
    unsafe_allow_html=True
)


selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <p style="font-size:16px; font-weight:bold; color:#00e0ff; margin-bottom:8px;">
                    {names[0]}
                </p>
                <img src="{posters[0]}" 
                     style="width:160px; height:240px; object-fit:cover; border-radius:8px;" />
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <p style="font-size:16px; font-weight:bold; color:#00e0ff; margin-bottom:8px;">
                    {names[1]}
                </p>
                <img src="{posters[1]}" 
                     style="width:160px; height:240px; object-fit:cover; border-radius:8px;" />
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <p style="font-size:16px; font-weight:bold; color:#00e0ff; margin-bottom:8px;">
                    {names[2]}
                </p>
                <img src="{posters[2]}" 
                     style="width:160px; height:240px; object-fit:cover; border-radius:8px;" />
            </div>
            """, unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <p style="font-size:16px; font-weight:bold; color:#00e0ff; margin-bottom:8px;">
                    {names[3]}
                </p>
                <img src="{posters[3]}" 
                     style="width:160px; height:240px; object-fit:cover; border-radius:8px;" />
            </div>
            """, unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <p style="font-size:16px; font-weight:bold; color:#00e0ff; margin-bottom:8px;">
                    {names[4]}
                </p>
                <img src="{posters[4]}" 
                     style="width:160px; height:240px; object-fit:cover; border-radius:8px;" />
            </div>
            """, unsafe_allow_html=True
        )



