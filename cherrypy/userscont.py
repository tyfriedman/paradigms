import cherrypy
import re, json

class UserController(object):

    def __init__(self, db):
        self.db = db

    def GET(self):
        output = dict()
        output['users'] = []
        output['result'] = 'success'
        try:
            for user_id, user in self.db.users.items():
                output['users'].append({'id': user_id, 'zipcode': user['zipcode'], 'age': user['age'], 'gender': user['gender'], 'occupation': user['occupation']})
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
            if not self.db.users:
                user_id = 1
            else:
                user_id = max([user_id for user_id in self.db.users.keys()]) + 1
            self.db.users[user_id] = {'zipcode': data['zipcode'], 'age': data['age'], 'gender': data['gender'], 'occupation': data['occupation'], 'rated_movies': []}
            output['id'] = user_id
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
    
    def DELETE(self):
        output = dict()
        output['result'] = 'success'
        try:
            self.db.users = dict()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)