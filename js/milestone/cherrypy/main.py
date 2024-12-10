from mdb import mdb
import pprint
import cherrypy
from moviescont import MovieController
from moviesidcont import MovieIdController
from userscont import UserController
from usersidcont import UserIdController
from resetcont import ResetController
from recommendationscont import RecommendationController
from recommendationsidcont import RecommendationIdController
from ratingsidcont import RatingIdController

class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def start_service(db):
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    movie_controller = MovieController(db)
    movie_id_controller = MovieIdController(db)
    user_controller = UserController(db)
    user_id_controller = UserIdController(db)
    reset_controller = ResetController(db)
    recommendation_controller = RecommendationController(db)
    recommendation_id_controller = RecommendationIdController(db)
    rating_id_controller = RatingIdController(db)
    options_controller = optionsController()
    
    # /reset/
    dispatcher.connect('reset_get', '/reset/', controller=reset_controller, action = 'PUT', conditions=dict(method=['PUT']))
    # /movies/
    dispatcher.connect('movies_get', '/movies/', controller=movie_controller, action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('movies_post', '/movies/', controller=movie_controller, action = 'POST', conditions=dict(method=['POST']))
    dispatcher.connect('movies_delete', '/movies/', controller=movie_controller, action = 'DELETE', conditions=dict(method=['DELETE']))
    # /movies/:movie_id
    dispatcher.connect('movies_id_get', '/movies/:movie_id', controller=movie_id_controller, action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('movies_id_put', '/movies/:movie_id', controller=movie_id_controller, action = 'PUT', conditions=dict(method=['PUT']))
    dispatcher.connect('movies_id_delete', '/movies/:movie_id', controller=movie_id_controller, action = 'DELETE', conditions=dict(method=['DELETE']))
    # /users/
    dispatcher.connect('users_get', '/users/', controller=user_controller, action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('users_post', '/users/', controller=user_controller, action = 'POST', conditions=dict(method=['POST']))
    dispatcher.connect('users_delete', '/users/', controller=user_controller, action = 'DELETE', conditions=dict(method=['DELETE']))
    # /users/:user_id
    dispatcher.connect('users_id_get', '/users/:user_id', controller=user_id_controller, action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('users_id_put', '/users/:user_id', controller=user_id_controller, action = 'PUT', conditions=dict(method=['PUT']))
    dispatcher.connect('users_id_delete', '/users/:user_id', controller=user_id_controller, action = 'DELETE', conditions=dict(method=['DELETE']))
    # /recommendations/
    dispatcher.connect('recommendations_delete', '/recommendations/', controller=recommendation_controller, action = 'DELETE', conditions=dict(method=['DELETE']))
    # /recommendations/:user_id
    dispatcher.connect('recommendations_id_get', '/recommendations/:user_id', controller=recommendation_id_controller, action = 'GET', conditions=dict(method=['GET']))
    dispatcher.connect('recommendations_id_put', '/recommendations/:user_id', controller=recommendation_id_controller, action = 'PUT', conditions=dict(method=['PUT']))
    # /ratings/:movie_id
    dispatcher.connect('ratings_id_get', '/ratings/:movie_id', controller=rating_id_controller, action = 'GET', conditions=dict(method=['GET']))

    conf = {'global': {'server.socket_host': 'student13.cse.nd.edu', 'server.socket_port': 51020}, '/': {'request.dispatch': dispatcher, 'tools.CORS.on': True}}
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    
    cherrypy.config.update(conf)

    dispatcher.connect('reset_options', '/reset/', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('movies_options', '/movies/', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('movies_id_options', '/movies/:movie_id', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('users_options', '/users/', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('users_id_options', '/users/:user_id', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))   
    dispatcher.connect('recommendations_options', '/recommendations/', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('recommendations_id_options', '/recommendations/:user_id', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('ratings_id_options', '/ratings/:movie_id', controller=options_controller, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    db = mdb()
    db.load_movies()
    db.load_users()
    db.load_ratings()

    start_service(db)
