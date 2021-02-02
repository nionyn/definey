import os
import sys
import definey
sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    response = definey.get_response(environ)
    response_header = [
        ('Content-Type', 'application/vnd.api+json')
    ]
    status = '200 OK' if 'data' in response else '422'
    start_response(status, response_header)
    return [response.encode('utf-8')]
