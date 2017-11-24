import random
import os, os.path
import string


import cherrypy

throttle = 0
turn = 0
class StringGenerator(object):



    @cherrypy.expose
    def index(self):
        return open("index.html")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def forward(self):
        global throttle
        throttle = 1

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def backward(self):
        global throttle
        throttle = -1

        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def left(self):
        global turn
        turn = -.5
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def right(self):
        global turn
        turn = .5

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def state(self):
        return [throttle, turn]

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def setState(self):
        input_json = cherrypy.request.json
        global throttle, turn
        throttle, turn = input_json




if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    cherrypy.quickstart(webapp, '/', conf)