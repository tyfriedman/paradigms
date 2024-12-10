import cherrypy
import re, json

class RatingIdController(object):

    def __init__(self, db):
        self.db = db

    def GET(self, movie_id):
        output = dict()
        output['result'] = 'success'
        try:
            movie_id = int(movie_id)
            output['rating'] = self.db.ratings[movie_id]['avg_rating']
            output['movie_id'] = movie_id
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
