#IMDB score is above 5.5

# Dictionary of movies

def is_above_5_5(movie):
    return movie['imdb'] > 5.5


movie = {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
}
print(is_above_5_5(movie))