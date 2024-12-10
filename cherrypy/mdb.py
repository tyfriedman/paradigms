class mdb(object):
    def __init__(self):
        self.movies = dict()
        self.users = dict()
        self.ratings = dict()

    def load_movies(self):
        with open("./data/movies.dat", 'r') as data:
            for movie in data:
                movie = movie.strip()
                movie = movie.split("::")
                self.movies[int(movie[0])] = {'title': movie[1], 'genres': movie[2], 'img': None, 'rating': 0}
        with open("./data/images.dat", 'r') as data:
            for image in data:
                image = image.strip()
                image = image.split("::")
                self.movies[int(image[0])]['img'] = image[2]

    def load_users(self):
        with open("./data/users.dat", 'r') as data:
            for user in data:
                user = user.strip()
                user = user.split("::")
                self.users[int(user[0])] = {'gender': user[1], 'age': int(user[2]), 'occupation': int(user[3]), 'zipcode': user[4], 'rated_movies': []}


    def load_ratings(self):
        self.ratings.clear()
        with open("./data/ratings.dat", 'r') as data:
            for rating in data:
                rating = rating.strip()
                rating = rating.split("::")
                movie_id = int(rating[1])
                if movie_id in self.ratings.keys():
                    self.ratings[movie_id]['ratings'].append(int(rating[2]))
                    self.ratings[movie_id]['user_votes'][int(rating[0])] = int(rating[2])
                else:
                    self.ratings[movie_id] = {'ratings': [int(rating[2])], 'user_votes': {int(rating[0]): int(rating[2])}}
                self.users[int(rating[0])]['rated_movies'].append(movie_id)
        for movie_id, ratings in self.ratings.items():
            ratings['avg_rating'] = sum(ratings['ratings']) / len(ratings['ratings'])
            if movie_id in self.movies:
                self.movies[movie_id]['rating'] = ratings['avg_rating']