# 🎵 Music Recommender Simulation

## Terminal Output Images

![Terminal Output]("codepath music rec.png")

User Preference Images:

![User Pref Pop]("chill pop.png")
![User Pref Rock]("happy rock.png")
![User Pref Ambient]("happy ambient.png")

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project examines user's preferences with genre, tempo, mood, and energy to produce a list of song recommendations. It utilizes a Gaussian distance based formula in order to produce scoring, and then weights the final scores.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Answer:
- Each `Song` in my system will store mood, energy, and tempo_bpm.
- Each `UserProfile` in my system will store the mean and standard deviation of the mood, energy, and tempo_bpm of the songs they listen to.
- For the recommender to score the songs, the recommender will compute the Gaussian value of each individual property, and then average all of the values.
- Finally, to choose which songs to recommend, after the songs have been scored, the songs will be sorted in descending order, with the highest scoring songs being the first to be recommended.

Potential Bias:
- Since the system weights the metrics equally to develop the score, it might lead to under-weighting of certain metrics like genre. Overall, it might lead to less realistic recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I tried many experiments varying the users preferences and found that users preference regarding categorical values tended to be more favored than their continuous property values. For example, in trying user preferences for different genres like ambient, rock, and pop, the users genres were always put first when explained.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

It tends to favor genre over other preferences that are more continuous, like tempo. Also, it was only provided a very small data source, limiting the types of recommendations.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

It was interesting learning about how the recommendation system evolves. It starts via preprocessing, then scoring, and then the weighting of those scores.

I learned a lot about how data sources influence system outputs. Because the original data source in the songs.csv were so few in number, many of the genres were few in number or were not even represented at all. This leads to restricted options/outputs being shown to users.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

SongRecs 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

This recommender generates song recommendations given user's preferences, which
are assumed to be genre, mood, energy, and tempo preferences. This is for classroom
exploration.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.


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

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

There are 15 total songs, and genres including pop, lofi, rock, ambient, jazz, electronic, indie pop as well as happy, chill, intense, relaxed, moody, focused moods. I did not add or remove data. There are parts of musical taste missing- specifically, genres like rap are not represented.

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

My system works well for users with a strong preference for genre over other preferences. My system also best captured the pattern of users who liked chill pop songs. The recommendation for chill pop songs also matched my intuition, and I believe this is because the data source best represented those categories.

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

The system most favors matches for genre and mood over other potential preferences (because exact matches for genre and mood are weighted heavily, more than the continous vairables), which can cause items like energy or tempo to be ignored. Additionally, because the pop category only considers exact matches instead of similar genres, this can ignore potentially better sub-fits. Additionally, because the grenre of pop is overrepresented in the sample, this may lead to biased recommendations.

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

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

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

I would vastly expand the data source that the model is drawing from in order to provide a wider variety of song recommendations and get more genres recommended. Better explainability would also be great in order to allow people to have more confidence in what the model is recommending.

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

I learned more about howing the preprocessing and then scoring phases of these recommender systems work. It also encouraged me to think more about how data sources influence model outputs. AI tools allowed me to debug and also get a great scoring formula, which was very helpful, but I still double-checked the output.

