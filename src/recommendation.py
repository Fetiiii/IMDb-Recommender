import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import time

class SeriesRecommender:
    def __init__(self, data_path="C:/Users/cagri/Desktop/f/IMDb ML/data/imdb_data.json"):
        """Initialize the recommender system"""
        print("Loading data and initializing model...")
        self.df = pd.read_json(data_path)
        
        # Rename columns to match our code
        self.df = self.df.rename(columns={
            'Dizi Adı': 'title',
            'IMDb Puanı': 'rating',
            'Link': 'link',
            'Çıkış Tarihi': 'release_date',
            'Türler': 'genres'
        })
        
        # Convert genres list to string
        self.df['genres'] = self.df['genres'].apply(lambda x: ' '.join(x) if isinstance(x, list) else x)
        
        # Clean title (remove numbering)
        self.df['title'] = self.df['title'].apply(lambda x: ' '.join(x.split()[1:]) if x.split()[0].endswith('.') else x)
        
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = None
        
    def prepare_features(self):
        """Prepare text features for embedding"""
        print("Preparing features...")
        # Combine title, genres for better context
        self.df['features'] = self.df['title'] + ' ' + self.df['genres']
        return self.df['features'].tolist()
    
    # ... [rest of the code remains the same] ...
    
    def generate_embeddings(self):
        """Generate embeddings using Sentence Transformer"""
        print("Generating embeddings... This may take a few minutes.")
        start_time = time.time()
        
        features = self.prepare_features()
        self.embeddings = self.model.encode(features)
        
        print(f"Embeddings generated in {time.time() - start_time:.2f} seconds")
        return self.embeddings
    
    def get_recommendations(self, title, n_recommendations=5):
        """Get series recommendations based on title"""
        if self.embeddings is None:
            self.generate_embeddings()
            
        # Find the index of the input title
        try:
            idx = self.df[self.df['title'].str.lower() == title.lower()].index[0]
        except IndexError:
            print(f"Error: '{title}' not found in database")
            return None
        
        # Calculate cosine similarities
        similarities = cosine_similarity([self.embeddings[idx]], self.embeddings)[0]
        
        # Get top N similar series indices (excluding the input series)
        similar_indices = similarities.argsort()[::-1][1:n_recommendations+1]
        
        # Create recommendations dataframe
        recommendations = self.df.iloc[similar_indices][['title', 'rating', 'genres', 'link']]
        
        return recommendations

def main():
    # Initialize recommender
    recommender = SeriesRecommender()
    
    while True:
        # Get user input
        title = input("\nEnter a TV series title (or 'quit' to exit): ")
        if title.lower() == 'quit':
            break
            
        # Get recommendations
        recommendations = recommender.get_recommendations(title)
        
        if recommendations is not None:
            print("\nTop 5 Similar TV Series:")
            print("-" * 50)
            for idx, row in recommendations.iterrows():
                print(f"Title: {row['title']}")
                print(f"Rating: {row['rating']}")
                print(f"Genres: {row['genres']}")
                print(f"IMDb Link: {row['link']}")
                print("-" * 50)

if __name__ == "__main__":
    main()