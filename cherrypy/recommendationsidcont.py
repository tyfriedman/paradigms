import cherrypy
import re, json

class RecommendationIdController(object):

    def __init__(self, db):
        self.db = db

    def GET(self, user_id):
        output = dict()
        output['result'] = 'success'
        try:
            user_id = int(user_id)
            rated_movies = self.db.users[user_id]['rated_movies']
            recommended_movie = max([movie_id for movie_id in self.db.movies.keys() if movie_id not in rated_movies and self.db.movies[movie_id]['rating']], key=lambda movie_id: self.db.movies[movie_id]['rating'])
            output['movie_id'] = recommended_movie
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    def PUT(self, user_id):
        output = dict()
        output['result'] = 'success'
        try:
            data = cherrypy.request.body.read().decode('utf-8')
            data = json.loads(data)
            user_id = int(user_id)
            rating = int(data['rating'])
            movie_id = int(data['movie_id'])
            self.db.ratings[movie_id]['user_votes'][user_id] = rating
            self.db.ratings[movie_id]['ratings'] = list(self.db.ratings[movie_id]['user_votes'].values())
            self.db.ratings[movie_id]['avg_rating'] = sum(self.db.ratings[movie_id]['ratings']) / len(self.db.ratings[movie_id]['ratings'])
            self.db.movies[movie_id]['rating'] = self.db.ratings[movie_id]['avg_rating']
            self.db.users[user_id]['rated_movies'].append(movie_id)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
