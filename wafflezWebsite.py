import random
import os, os.path
from cherrypy.lib import static


import cherrypy

throttle = 0
turn = 0
zephyr = "No recent zephyrs"
faces = {"happy": 'static/waffles_happy.png', 
         "confused": 'static/waffles_confused.png',
         "playful": 'static/waffles_playful.png',
         "neutral": 'static/waffles_neutral.png',
         "sad": 'static/waffles_sad.png',
         "sleep": 'static/waffles_sleep.png'}
face = 'neutral'


def get_image(path):
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = canonicalized_path

        return image

class StringGenerator(object):

    @cherrypy.expose
    def index(self):
        global zephyr
        index = open("index.html").read().format(face=faces[face], z=zephyr)
        return index

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
    @cherrypy.tools.json_out()
    def get_zephyr(self):
        print("GOTTEN")
        return zephyr

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def set_state(self):
        input_json = cherrypy.request.json
        global throttle, turn
        throttle, turn = input_json

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def set_zephyr(self):
        input_json = cherrypy.request.json
        global zephyr
        zephyr = input_json

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def set_mood(self):
        
        input_json = cherrypy.request.json
        global faces, face
        face = input_json
        


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
            'tools.staticdir.dir': 'faces'
        }
    }
    webapp = StringGenerator()
    cherrypy.quickstart(webapp, '/', conf)