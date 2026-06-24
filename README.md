# 📚 BookSphere — Book Recommender System



<p>
  A full-stack machine learning web application that recommends books using <b>Collaborative Filtering</b> powered by cosine similarity — built with Python, Flask, and a custom dark-themed UI.
</p>

---

## 🌟 Live Demo

> `https://book-recommender-system-mucgfdkambzqw9r5i3mf3x.streamlit.app`

---

## ✨ Features

- 🏠 **Home Page** — Displays the **Top 50 most popular books** filtered by minimum 250 ratings and sorted by average rating
- 🔍 **Recommend Page** — Enter any book title and get **4 similar book recommendations** powered by collaborative filtering
- 🤝 **Collaborative Filtering** — Uses a user-item pivot table and cosine similarity to find books liked by similar readers
- 💻 **Modern Dark UI** — Custom HTML/CSS with smooth animations, and responsive layout

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.9+, Flask |
| **ML / Data** | Pandas, NumPy |
| **Algorithm** | Collaborative Filtering + Cosine Similarity |
| **Frontend** | HTML, CSS |
| **Serialization** | Pickle |
| **Dataset** | Book Recommendation Dataset (Kaggle) |

---

## 📁 Project Structure

```
book-recommender-system/
│
├── app.py                          # Flask backend & routes
├── book-recommender-system.ipynb   # Data processing & model training notebook
│
├── templates/
│   ├── index.html                  # Home — Top 50 popular books
│   └── recommend.html              # Recommend — Collaborative filtering UI
│
├── popular.pkl                     # Serialized popular books dataframe
├── pt.pkl                          # Pivot table (users × books)
├── books.pkl                       # Books metadata
├── similarity_scores.pkl           # Pre-computed cosine similarity matrix
│
└── README.md
```

---

## 🧠 How It Works

### 1. Popularity-Based (Home Page)

Books are ranked using:
1. Filter books with **≥ 250 ratings** (removes low-signal titles)
2. Calculate **average rating** per book
3. Display the **Top 50** sorted by average rating

```python
popular_df = popular_df[popular_df['num_ratings'] >= 250]
              .sort_values('avg_rating', ascending=False)
              .head(50)
```

### 2. Collaborative Filtering (Recommend Page)

Based on the **Memory-Based Collaborative Filtering** approach:

1. Build a **User-Item Matrix** (pivot table of user ratings per book)
2. Compute **Cosine Similarity** between all books
3. For a given book, find the **top-4 most similar books** by similarity score

```python
index = np.where(pt.index == user_input)[0][0]
similar_items = sorted(
    list(enumerate(similarity_scores[index])),
    key=lambda x: x[1],
    reverse=True
)[1:5]
```

---

## 📊 Dataset

**Book-Crossing Dataset** — Collected by Cai-Nicolas Ziegler (2004)

| File | Records |
|---|---|
| `Books.csv` | 271,379 books |
| `Users.csv` | 278,858 users |
| `Ratings.csv` | 1,149,780 ratings |

Source: [Kaggle — Book-Crossing Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

---






