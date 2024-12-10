import cherrypy
import re, json

class ResetController(object):

    def __init__(self, db):
        self.db = db

    def PUT(self):
        output = {'result':'success'}
        try:
            self.db.load_movies()
            self.db.load_users()
            self.db.load_ratings()
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output)