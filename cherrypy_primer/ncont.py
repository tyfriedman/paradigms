import cherrypy
import re, json

class NameController(object):
    def __init__(self):
        self.myd = dict()

    def GET(self):
        output = {'result':'success'}
        try:
            output['name'] = 'Ty Friedman'
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'error message'
        return json.dumps(output)