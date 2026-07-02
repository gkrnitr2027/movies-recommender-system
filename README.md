# 🎬 Movie Recommender System

A content-based movie recommendation system built using Machine Learning and NLP. The application recommends movies similar to the one selected by the user based on movie metadata such as genres, keywords, cast, crew, and overview.

## Features

* Content-based movie recommendations
* Movie selection through an interactive Streamlit interface
* NLP-based feature extraction
* Cosine similarity for finding similar movies
* Clean and simple UI

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

## Dataset

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

## Project Structure

```text
Movie-Recommender-System/
│── app.py
│── Movie-recommender-system.ipynb
│── movie_dict.pkl
│── movies.pkl
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
└── README.md
```
## Generate the Similarity Matrix

The `similarity.pkl` file is **not included** in this repository because its size exceeds GitHub's 100 MB file upload limit.

To generate it locally:

1. Open `Movie-recommender-system.ipynb`.
2. Run all notebook cells from start to finish.
3. This will generate:

   * `movie_dict.pkl`
   * `similarity.pkl`
4. Ensure both files are present in the project directory.

## Run the Application

```bash
streamlit run app.py
```

## How It Works

1. Load and merge the TMDB datasets.
2. Preprocess movie metadata using NLP techniques.
3. Create tags by combining important movie features.
4. Convert text into vectors using CountVectorizer.
5. Compute cosine similarity between movie vectors.
6. Recommend the top 5 most similar movies.

## Note

The file `similarity.pkl` is intentionally excluded from this repository because it is approximately **176 MB**, which exceeds GitHub's maximum file size limit of **100 MB**.

You can regenerate it locally by executing the notebook before running the Streamlit application.
