"""                 RECOMMENDATION SYSTEM
    Create a simple recommendation system that suggests items to
    users based on their preferences. You can use techniques like
    collaborative filtering or content-based filtering to recommend
    movies, books, or products to users                         """


"""                         BOOK RECOMMENDATION SYSTEM                            """
import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
import os

# Get the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load your data into pandas DataFrames
book_id_map = pd.read_csv(os.path.join(dir_path, 'book_id_map.csv'))
book_titles = pd.read_csv(os.path.join(dir_path, 'book_titles.csv'))
collab_book_metadata = pd.read_csv(os.path.join(dir_path, 'collaborative_book_metadata.csv'))
collab_books_df = pd.read_csv(os.path.join(dir_path, 'collaborative_books_df.csv'))
user_id_map = pd.read_csv(os.path.join(dir_path, 'user_id_map.csv'))

# Merge the dataframes based on book_id
merged_df = pd.merge(collab_books_df, collab_book_metadata, on='book_id')

# Create a pivot table with users as rows and books as columns
pivot_table = merged_df.pivot_table(index='user_id_mapping', columns='name', values='Actual Rating').fillna(0)

# Normalize the values
pivot_table_normalized = pivot_table - pivot_table.mean()

# Convert the DataFrame to a numpy ndarray
pivot_table_normalized_np = pivot_table_normalized.to_numpy()

# Apply SVD
U, sigma, Vt = svds(pivot_table_normalized_np, k=50)
sigma = np.diag(sigma)

# Initialize predicted_ratings and cf_preds_df to None
predicted_ratings = None
cf_preds_df = pd.DataFrame()

# Check if U, sigma, and Vt are not None and are of the correct type
if U is not None and sigma is not None and Vt is not None and isinstance(U, np.ndarray) and isinstance(sigma, np.ndarray) and isinstance(Vt, np.ndarray):
    # Calculate the dot product to get the reconstructed matrix
    predicted_ratings = np.dot(np.dot(U, sigma), Vt) + pivot_table.mean().values
else:
    print("Error: U, sigma, or Vt is None or not of the correct type")

# If predicted_ratings is not None, convert the reconstructed matrix back to a DataFrame
if predicted_ratings is not None:
    cf_preds_df = pd.DataFrame(predicted_ratings, columns=pivot_table.columns, index=pivot_table.index)
else:
    print("Error: predicted_ratings is None")

# Function to recommend books to a user based on matrix factorization
def recommend_books():
    # Take user input for user_id_mapping
    try:
        user_id_mapping = int(input("Enter the user id (user_id_mapping) : "))
    except ValueError:
        print("Invalid user id entered.")
        return
    
    # Check if the user_id_mapping is valid (exists in the dataset)
    if user_id_mapping not in cf_preds_df.index:
        print(f"Error: User with user id (user_id_mapping) {user_id_mapping} not found.")
        return
    
    # Get the recommended books for the user
    sorted_user_predictions = cf_preds_df.loc[user_id_mapping].sort_values(ascending=False)
    recommended_books = pd.DataFrame(sorted_user_predictions).reset_index().rename(columns={user_id_mapping: 'Predicted Rating'})
    
    # Shift the index to start from 1 instead of 0
    recommended_books.index += 1
    
    # Display the top recommended books
    print(recommended_books.head(10))

# Call the function to recommend books based on user input
recommend_books()
