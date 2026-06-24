import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="BookSphere - Book Recommender",
    page_icon="📚",
    layout="wide"
)

@st.cache_resource
def load_data():
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
    return popular_df, pt, books, similarity_scores

popular_df, pt, books, similarity_scores = load_data()

page = st.sidebar.radio("Navigate", ["🏠 Home - Top 50 Books", "✨ Recommend a Book"])

if page == "🏠 Home - Top 50 Books":
    st.title("📚 Top 50 Books")
    st.markdown("*Curated from 270,000+ readers · Minimum 250 ratings*")
    st.divider()

    cols_per_row = 5
    for i in range(0, len(popular_df), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(popular_df):
                with col:
                    try:
                        st.image(popular_df['Image-URL-M'].values[idx], use_column_width=True)
                    except:
                        st.write("📖")
                    st.caption(f"**{popular_df['Book-Title'].values[idx][:35]}...**"
                               if len(popular_df['Book-Title'].values[idx]) > 35
                               else f"**{popular_df['Book-Title'].values[idx]}**")
                    st.caption(f"✍️ {popular_df['Book-Author'].values[idx]}")
                    st.caption(f"⭐ {popular_df['avg_rating'].values[idx]:.1f} · {popular_df['num_ratings'].values[idx]} votes")

else:
    st.title("✨ Find Your Next Read")
    st.markdown("*Enter a book you love and get 4 similar recommendations*")
    st.divider()

    user_input = st.text_input("Enter a book title:", placeholder="e.g. Harry Potter and the Chamber of Secrets")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("The Da Vinci Code"): user_input = "The Da Vinci Code"
    with col2:
        if st.button("The Notebook"): user_input = "The Notebook"
    with col3:
        if st.button("A Walk to Remember"): user_input = "A Walk to Remember"
    with col4:
        if st.button("Harry Potter"): user_input = "Harry Potter and the Chamber of Secrets"

    if st.button("🔍 Find Similar Books", type="primary"):
        if user_input:
            try:
                index = np.where(pt.index == user_input)[0][0]
                similar_items = sorted(
                    list(enumerate(similarity_scores[index])),
                    key=lambda x: x[1], reverse=True
                )[1:5]

                st.success(f"Found {len(similar_items)} books similar to '{user_input}'")
                st.divider()

                cols = st.columns(len(similar_items))
                for i, (item_idx, score) in enumerate(similar_items):
                    book_title = pt.index[item_idx]
                    temp_df = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')
                    with cols[i]:
                        try:
                            st.image(temp_df['Image-URL-M'].values[0], use_column_width=True)
                        except:
                            st.write("📖")
                        st.markdown(f"**{book_title}**")
                        st.caption(f"✍️ {temp_df['Book-Author'].values[0]}")
                        st.caption(f"Similarity: {score:.2f}")
            except IndexError:
                st.error("Book not found in dataset. Please check the title and try again.")
        else:
            st.warning("Please enter a book title first.")