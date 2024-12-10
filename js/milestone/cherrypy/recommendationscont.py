import cherrypy
import re, json

class RecommendationController(object):

    def __init__(self, db):
        self.db = db

    def DELETE(self):
        output = dict()
        output['result'] = 'success'
        try:
            self.db.ratings.clear()
            for user_id in self.db.users.keys():
                self.db.users[user_id]['rated_movies'] = []
            for movie_id in self.db.movies.keys():
                self.db.movies[movie_id]['rating'] = 0
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)