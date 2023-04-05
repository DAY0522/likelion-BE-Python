import movies 
import random

movie = movies.Movie
cinema = movies.Cinema


class RandomCinema(movie, cinema):
    def __init__(self, name, genre, produce):
        movie.__init__(self,name, genre, produce)
        cinema.__init__(self)

    
    def get_cinema(self):
        random_cinema = random.choice(self.cinema_list)
        print(self.name,random_cinema)





test = RandomCinema( 'Spiderman',"action","someone")

test.get_cinema()