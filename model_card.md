# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

SongRecs 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender generates song recommendations given user's preferences, which
are assumed to be genre, mood, energy, and tempo preferences. This is for classroom
exploration.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The following features are used:

- Genre
- Mood
- Energy
- Tempo

These are also the same user preferences that are considered.

The model takes user preferences and compares them to the actual song statistics, using a formula derived from the distance from the personal preference to the song value (a Gaussian-based formula). Smaller distance leads to higher scores, and vice versa. The highest scores are then recommended.

User preference logic were changed from the initial to prioritize a smaller number of features, specifically the 4 listed above.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are 15 total songs, and genres including pop, lofi, rock, ambient, jazz, electronic, indie pop as well as happy, chill, intense, relaxed, moody, focused moods. I did not add or remove data. There are parts of musical taste missing- specifically, genres like rap are not represented.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

My system works well for users with a strong preference for genre over other preferences. My system also best captured the pattern of users who liked chill pop songs. The recommendation for chill pop songs also matched my intuition, and I believe this is because the data source best represented those categories.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 

The system most favors matches for genre and mood over other potential preferences (because exact matches for genre and mood are weighted heavily, more than the continous vairables), which can cause items like energy or tempo to be ignored. Additionally, because the pop category only considers exact matches instead of similar genres, this can ignore potentially better sub-fits. Additionally, because the grenre of pop is overrepresented in the sample, this may lead to biased recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Note: My screenshots for this were included at the top of the document.

I tested three different user profiles. Each had a different genre (pop, rock, and ambient) as well as different mixes of energy, tempo, and mood. Ultimately, what surprised me was how genre matches consistently were the highest ranked, which after analysis was due to the fact that it was a categorical variable and thus an exact match was weighted heavily. 

Calm pop beats profile:

- Favored Gym Hero because it is a pop genre, with matches of energy and tempo being the next highest with Rooftop Lights and Bassline Theory.

Happy ambient sounds profile:

- Favored Morning Mist and Spacewalk Thoughts because both songs were from the same genre, ambient.

Happy rock profile:

- Favored Storm Runner because it was the matched genre, rock. But likely because it had the same mood as the previous, it had the same second recommended song, Morning Mist.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would vastly expand the data source that the model is drawing from in order to provide a wider variety of song recommendations and get more genres recommended. Better explainability would also be great in order to allow people to have more confidence in what the model is recommending.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned more about howing the preprocessing and then scoring phases of these recommender systems work. It also encouraged me to think more about how data sources influence model outputs. AI tools allowed me to debug and also get a great scoring formula, which was very helpful, but I still double-checked the output.
