import difflib
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('movies.csv')
selected_columns = ['genres' , 'keywords','tagline','cast','director']
for feature in selected_columns:
    df[feature] = df[feature].fillna('')

combined_feature = ''
for feature in selected_columns:
    combined_feature = combined_feature + df[feature] +' '
vectorizer = TfidfVectorizer()
vect_feature = vectorizer.fit_transform(combined_feature)
similarity = cosine_similarity(vect_feature)

all_movies = df['title'].tolist() 


def recommendation_system(name):
   closest_match = difflib.get_close_matches(name , all_movies)
   closest_match = closest_match[0]
   index = df[df.title == closest_match]['index'].values[0]
   similarity_score = list(enumerate(similarity[index]))
   sorted_similarity_score = sorted(similarity_score , key = lambda x:x[1] , reverse=True)
   i = 1
   for movies in sorted_similarity_score:
       index = movies[0]
       title  = df[df.index == index]['title'].values[0]
       poster_url = None
       poster_url = df[df.index == index]['homepage'].values[0]
       if(i < 31):
           cols = st.columns([1, 5])
           with cols[0]:
               if poster_url and isinstance(poster_url, str) and poster_url.strip():
                   st.image(poster_url, width=80)
           with cols[1]:
               st.write(f"{i}. {title}")
           i += 1

def main():
    st.title('Movie Recommendation System')
    st.subheader('Find your next favorite movie!')

    selected_movie = st.selectbox('Select a movie:', all_movies)

    if st.button('Recommend'):
        st.write(f'Recommending movies similar to: {selected_movie}')
        recommendation_system(selected_movie)

if __name__ == '__main__':
    main()