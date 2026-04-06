"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs

def main() -> None:
    # Load the dataset
    songs = load_songs("data/songs.csv") 
    
    # Updated to match the logic: favorite_genre, preferred_mood, target_energy, target_tempo
    user_prefs = {
        "favorite_genre": "pop", 
        "preferred_mood": "happy", 
        "target_energy": 0.8,
        "target_tempo": 120.0
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*50)
    print(f"{'MUSIC RECOMMENDATION ENGINE':^50}")
    print("="*50)
    print(f"Target: {user_prefs['favorite_genre']} | {user_prefs['preferred_mood']} | Energy: {user_prefs['target_energy']}")
    print("-" * 50)

    if not recommendations:
        print("No recommendations found. Check your data path!")
        return

    for i, (song, score, explanation) in enumerate(recommendations, 1):
        # Header for the song
        header = f"{i}. {song['title'].upper()}"
        print(f"{header:<35} SCORE: {score:.2f}")
        
        # Metadata line
        metadata = f"   Artist: {song['artist']} | Genre: {song['genre']}"
        print(metadata)
        
        # Explanation line
        print(f"   Why: {explanation}")
        
        # Divider between songs (except for the last one)
        if i < len(recommendations):
            print(f"   {'-' * 44}")

    print("="*50 + "\n")

if __name__ == "__main__":
    main()