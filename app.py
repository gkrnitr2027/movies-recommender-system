import streamlit as st
import pickle
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main{
    background-color:#0E1117;
}
h1{
    text-align:center;
    color:#00C6FF;
}
.stButton>button{
    width:100%;
    background:#00C6FF;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}
.stButton>button:hover{
    background:#0096c7;
}
.movie-box{
    background:#262730;
    padding:15px;
    border-radius:12px;
    text-align:center;
    color:white;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Load Data ----------------
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- Recommendation Function ----------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations

# ---------------- Header ----------------
st.title("🎬 Movie Recommendation System")

st.markdown(
"""
<center>
Find movies similar to your favourite one using Machine Learning.
</center>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- Select Movie ----------------
selected_movie = st.selectbox(
    "Choose a Movie",
    movies["title"].values
)

# ---------------- Button ----------------
if st.button("🎥 Recommend Movies"):

    recommended_movies = recommend(selected_movie)

    st.write("")
    st.subheader("Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for col, movie in zip(cols, recommended_movies):
        with col:
            st.markdown(
                f"<div class='movie-box'>{movie}</div>",
                unsafe_allow_html=True
            )