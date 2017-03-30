# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story','Story of a boy','https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg','https://www.youtube.com/watch?v=ZZv1vki4ou4')

avatar = media.Movie('Avatar','A Marine sent for a mission on an alien planet','https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg','https://www.youtube.com/watch?v=5PSNL1qE6VY')

shawshank_redemption=media.Movie('Shawshank Redemption','An accountant who flees from a Prison','https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg','https://www.youtube.com/watch?v=NmzuHjWmXOc')

movies = [toy_story, avatar,shawshank_redemption]
fresh_tomatoes.open_movies_page(movies)
#print avatar.storyline
#movies[1].show_trailer()

