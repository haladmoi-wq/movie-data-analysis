import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("movies.csv")

# Basic statistics
print(data)

print("\nAverage rating:", data["rating"].mean())
print("Average duration:", data["duration"].mean())

# Average rating by genre
genre_rating = data.groupby("genre")["rating"].mean()

print("\nAverage rating by genre:")
print(genre_rating)

# Bar chart: Average rating by genre
genre_rating.plot(kind="bar")

plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# Scatter plot: Duration vs Rating
plt.figure()
plt.scatter(data["duration"], data["rating"])

plt.title("Movie Duration vs Rating")
plt.xlabel("Duration (minutes)")
plt.ylabel("Rating")

plt.tight_layout()
plt.show()

# Top 5 highest-rated movies
top_movies = data.sort_values("rating", ascending=False).head(5)

print("\nTop 5 Highest-Rated Movies:")
print(top_movies[["title", "rating"]])