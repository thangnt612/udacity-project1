"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    print('-----------------------------'+HOST+'-----------------------------')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        print(PORT)
    except ValueError:
        PORT = 5555
    print(HOST)
    print(PORT)
    app.run(HOST, PORT, debug=True, ssl_context='adhoc')
