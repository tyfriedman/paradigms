import cherrypy
from ncont import NameController

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    nameController = NameController()

    # dictionaryController = DictionaryController()

    dispatcher.connect('name_get', '/name/', controller=nameController,
                            action = 'GET', conditions=dict(method=['GET']))

    conf = {'global': {'server.socket_host': 'student05.cse.nd.edu',
                       'server.socket_port': 51020},
            '/': {'request.dispatch': dispatcher}}
    
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    start_service()