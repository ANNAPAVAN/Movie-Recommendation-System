import streamlit as st
import pickle
import pandas as pd

def recommand(movie):
  movie_index = movies[movies["title"] == movie].index[0]
  distances = similarity[movie_index] 
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

  recommended_movies = []
  for i in movies_list:
        
    recommended_movies.append(movies.iloc[i[0]].title)

  return recommended_movies



movies_dict = pickle.load(open("../Files/movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("../Files/similarity.pkl", "rb"))



st.title("Movie Recommander System")

selected_movie_name = st.selectbox(
    "Movie Name",
    movies["title"].values
)

if st.button("Recommand"):
    recommandations = recommand(selected_movie_name)
    for i in recommandations:
      st.write(i)







