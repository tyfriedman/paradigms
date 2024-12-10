import cherrypy
import re, json

class MovieController(object):

    def __init__(self, db):
        self.db = db

    def GET(self):
        output = dict()
        output['movies'] = []
        output['result'] = 'success'
        try:
            for movie_id, movie in self.db.movies.items():
                output['movies'].append({'id': movie_id, 'genres': movie['genres'], 'title': movie['title'], 'img': movie['img'], 'result': 'success'})
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
    
    def POST(self):
        output = dict()
        output['result'] = 'success'
        try:
            data = cherrypy.request.body.read().decode('utf-8')
            data = json.loads(data)
            if not self.db.movies:
                movie_id = 1
            else:
                movie_id = max([movie_id for movie_id in self.db.movies.keys()]) + 1
            self.db.movies[movie_id] = {'genres': data['genres'], 'title': data['title'], 'img': '', 'rating': ''}
            output['id'] = movie_id
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
    
    def DELETE(self):
        output = dict()
        output['result'] = 'success'
        try:
            self.db.movies.clear()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)