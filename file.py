import pandas as pd 
import numpy as np 
import streamlit as st
import pandas as pd
import pickle
from dict import selected_books,d
from dict import sel_books
from dict import dic_book

a=np.load('data_array1.npy')
from sklearn.metrics.pairwise import cosine_similarity

def bert_recommend(target_book_title):
    target_book_index = dic_book.index(target_book_title)
    target_book_avg_embedding=a[target_book_index]
    similarities = cosine_similarity(a[target_book_index].reshape(1,-1), a)
    similar_books_indices = np.argsort(similarities[0])[::-1]
    similar_books_indices = similar_books_indices[similar_books_indices != target_book_index]
    top_n = 10  # Number of similar books to recommend
    recommended_unique_books_indices = similar_books_indices[:top_n]
    lst=[]
    for idx in recommended_unique_books_indices:
        lst.append(dic_book[idx])
    return lst 

# Define the spacing width between images 
space_width = 20  # in pixels

st.title("Book Recommendation For You")

books=st.selectbox("Please enter a book",sel_books)

images = d[books]
num_images = len(images)
    
# Calculate the number of columns in each row to create in the layout
num_columns = 5
columns = [st.columns(num_columns) for _ in range((num_images + num_columns - 1) // num_columns)]
    
for i, col in enumerate(columns):
    for j in range(num_columns):
        index = i * num_columns + j
        if index < num_images:
            try:
                col[j].image(images[index], use_column_width=True)
            except:
                col[j].write("Image not Available")
        else:
            col[j].write(" " * space_width)  # Create spacing

if st.button("Submit"):
    recmd=bert_recommend(books)

    for book in recmd:
        st.header(book)
    
        images = d[book]
        num_images = len(images)
    
        # Calculate the number of columns in each row to create in the layout
        num_columns = 4  
        columns = [st.columns(num_columns) for _ in range((num_images + num_columns - 1) // num_columns)]
    
        for i, col in enumerate(columns):
            for j in range(num_columns):
                index = i * num_columns + j
                if index < num_images:
                    try:
                        col[j].image(images[index], use_column_width=True)
                    except:
                        col[j].write("Image not Available")
                else:
                    col[j].write(" " * space_width)  # Create spacing

    st.write("Book selected succesfully")
