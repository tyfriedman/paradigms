import cherrypy
import re, json

class MovieIdController(object):

    def __init__(self, db):
        self.db = db

    def GET(self, movie_id):
        output = dict()
        output['result'] = 'success'
        try:
            movie_id = int(movie_id)
            output['id'] = movie_id
            output['title'] = self.db.movies[movie_id]['title']
            output['genres'] = self.db.movies[movie_id]['genres']
            output['img'] = self.db.movies[movie_id]['img']
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    def PUT(self, movie_id):
        output = dict()
        output['result'] = 'success'
        try:
            data = cherrypy.request.body.read().decode('utf-8')
            data = json.loads(data)
            movie_id = int(movie_id)
            self.db.movies[movie_id] = {'title': data['title'], 'genres': data['genres'], 'img': '', 'rating': 0}
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    def DELETE(self, movie_id):
        output = dict()
        output['result'] = 'success'
        try:
            movie_id = int(movie_id)
            del self.db.movies[movie_id]
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)