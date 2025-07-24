# Movie Recommendation System

This project is a simple content-based movie recommendation system built with Python. It allows users to get movie recommendations based on similarity scores calculated from movie metadata.

## Features

- Content-based filtering using TF-IDF and cosine similarity.
- Web interface powered by Streamlit.
- Dataset: `movies.csv` containing movie titles and other metadata.

## Files

- `app.py` – Streamlit web application to display the recommendations.
- `movie recommendation.ipynb` – Jupyter notebook for data exploration and model building.
- `movies.csv` – Dataset used for building the recommendation engine.

## How It Works

The recommender system uses:
- **TF-IDF Vectorization** on movie descriptions (e.g., genres, keywords, cast, etc.)
- **Cosine Similarity** to calculate similarity between movies.

## Getting Started

### Prerequisites

Ensure you have Python 3.7 or later installed.

### Installation

1. Clone the repository or download the project files.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
streamlit run app.py
```

This will launch the web interface in your browser.

## Example

Enter a movie title like `"The Matrix"` to get a list of similar movies based on metadata similarity.

## Author

- Syed Gufran Hussain


# movie_recommendation_app
