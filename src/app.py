import streamlit as st
from recommendation import SeriesRecommender

@st.cache_resource
def load_recommender():
    return SeriesRecommender()

def main():
    st.title("TV Series Recommender")
    
    # Initialize recommender
    recommender = load_recommender()
    
    # User input
    title = st.text_input("Enter a TV series title:")
    
    if title:
        recommendations = recommender.get_recommendations(title)
        
        if recommendations is not None:
            st.subheader("Recommended TV Series")
            
            for idx, row in recommendations.iterrows():
                with st.expander(f"{row['title']} (Rating: {row['rating']})"):
                    st.write(f"**Genres:** {row['genres']}")
                    st.write(f"**IMDb Link:** {row['link']}")

if __name__ == "__main__":
    main()