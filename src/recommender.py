import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_tempo: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs
        
    def _gaussian_score(self, value: float, preferred: float, sigma: float = 0.1) -> float:
        """Calculates a score between 0 and 1 based on proximity to a preferred value."""
        if sigma == 0: return 1.0 if value == preferred else 0.0
        return math.exp(-((value - preferred) ** 2) / (2 * sigma ** 2))

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Recommends songs based on user preferences.
        Required by tests/test_recommender.py
        """
        scored_songs = []

        for song in self.songs:
            # 1. Categorical Matches (1.0 if match, 0.0 otherwise)
            genre_score = 1.0 if song.genre == user.favorite_genre else 0.0
            mood_score = 1.0 if song.mood == user.preferred_mood else 0.0

            # 2. Continuous Gaussian Scores
            # We use a larger sigma for tempo since it has a wider range (e.g., 60-160)
            energy_score = self._gaussian_score(song.energy, user.preferred_energy, sigma=0.15)
            tempo_score = self._gaussian_score(song.tempo_bpm, user.preferred_tempo, sigma=20.0)

            # 3. Average the metrics
            final_score = (genre_score + mood_score + energy_score + tempo_score) / 4
            scored_songs.append((song, final_score))

        # Sort by score in descending order and return top k
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Provides an explanation for why a song was recommended.
        Required by src/main.py
        """
        match_reasons = []
        if song.genre == user.favorite_genre:
            match_reasons.append(f"it matches your love for {song.genre}")
        if song.mood == user.favorite_mood:
            match_reasons.append(f"it fits your current {song.mood} mood")
        
        if not match_reasons:
            return f"This song matches your preferred energy and tempo levels."
        
        return f"We recommended this because {' and '.join(match_reasons)}."

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    
    data = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                processed_row = {}
                for key, value in row.items():
                    # Strip whitespace to prevent conversion errors
                    val = value.strip()
                    
                    try:
                        # Attempt numerical conversion
                        if '.' in val:
                            processed_row[key] = float(val)
                        else:
                            processed_row[key] = int(val)
                    except ValueError:
                        # If conversion fails (e.g., for 'artist' names), keep as string
                        processed_row[key] = val
                        
                data.append(processed_row)
                
    except FileNotFoundError:
        print(f"Error: The file at {csv_path} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
        
    return data

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # 1. Convert song dictionaries to Song dataclass objects
    song_objects = [Song(**s) for s in songs]
    
    # 2. Convert user_prefs dictionary to UserProfile dataclass
    # Note: Mapping dict keys to dataclass fields
    user_profile = UserProfile(
        favorite_genre=user_prefs.get('favorite_genre'),
        favorite_mood=user_prefs.get('favorite_mood'),
        target_energy=user_prefs.get('target_energy', 0.5),
        target_tempo=user_prefs.get('target_tempo', 120.0)
    )
    
    # 3. Use the Recommender class to handle logic
    recommender = Recommender(song_objects)
    
    # We need scores and explanations, so we'll perform a custom sort 
    # using the internal helper methods of Recommender
    results = []
    for s_obj, s_dict in zip(song_objects, songs):
        # Calculate score
        g_score = (
            (1.0 if s_obj.genre == user_profile.favorite_genre else 0.0) +
            (1.0 if s_obj.mood == user_profile.favorite_mood else 0.0) +
            recommender._gaussian_score(s_obj.energy, user_profile.target_energy, 0.15) +
            recommender._gaussian_score(s_obj.tempo_bpm, user_profile.target_tempo, 20.0)
        ) / 4
        
        # Get explanation
        explanation = recommender.explain_recommendation(user_profile, s_obj)
        results.append((s_dict, round(g_score, 4), explanation))

    # 4. Sort from highest to lowest score and return top k
    return sorted(results, key=lambda x: x[1], reverse=True)[:k]
    
