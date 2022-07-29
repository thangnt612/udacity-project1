"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app
HOST = 'localhost'
PORT = 5555
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    print('-----------------------------'+HOST+'-----------------------------')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        print(PORT)
    except ValueError:
        PORT = 5555
app.run(HOST, PORT, ssl_context='adhoc')
#app.run(HOST, PORT, debug=True)
