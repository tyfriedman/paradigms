import cherrypy
import re, json

class UserIdController(object):

    def __init__(self, db):
        self.db = db

    def GET(self, user_id):
        output = dict()
        output['result'] = 'success'
        try:
            user_id = int(user_id)
            output['id'] = user_id
            output['zipcode'] = self.db.users[user_id]['zipcode']
            output['age'] = self.db.users[user_id]['age']
            output['gender'] = self.db.users[user_id]['gender']
            output['occupation'] = self.db.users[user_id]['occupation']
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
            self.db.users[user_id] = {'zipcode': data['zipcode'], 'age': int(data['age']), 'gender': data['gender'], 'occupation': int(data['occupation']), 'rated_movies': []}
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    def DELETE(self, user_id):
        output = dict()
        output['result'] = 'success'
        try:
            user_id = int(user_id)
            del self.db.users[user_id]
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)