import streamlit as st
import nltk
import sklearn
import pandas as pd
import pickle
import joblib

st.title('Movie Recomandation system')

with open("movies.pickle",'rb') as m:
    movies=pickle.load(m)

similarities=joblib.load("similarity.joblib")
movie_names= movies['title'].values

def recomand(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    recomandations=similarities[movie_index]
    movie_list=sorted(enumerate(recomandations),reverse=True,key=lambda x:x[1])[1:6]
    recomanded_movies=[]
    for i in movie_list:
        recomanded_movies.append(movies.iloc[i[0]].title)
    return recomanded_movies

name_movie=st.selectbox("Enter movie name",movie_names)

if st.button("Recomand"):
    r=recomand(name_movie)
    st.write("The recomanded movies are :")
    for i in r:
        st.write(i)