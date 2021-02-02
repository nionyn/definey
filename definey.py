from urllib.parse import parse_qs
from PyDictionary import PyDictionary
import json

def get_response(environ):
    # Get the variables word and function from the the query string e.g. word=cat&function=meaning 
    enviroment_variables = parse_qs(environ['QUERY_STRING'])
    word = enviroment_variables['word'][0] if 'word' in enviroment_variables else False   
    func = enviroment_variables['function'][0] if 'function' in enviroment_variables else False 
    
    # Map func variable to dictionary function and if not exist throw error
    dictionary=PyDictionary()
    function_list = {
        'meaning' : dictionary.meaning, 
        'synonym' : dictionary.synonym, 
        'antonym' : dictionary.antonym
    } 
    if func not in function_list:
        return make_output(error=True, message='Invalid function or function not set')

    # After a valid function has been acertained, run it with the search word, if no word found throw error
    data = function_list[func](word)
    if not data:
        return make_output(error=True, message='Word does not exist in database or word not set')
    else:
        return make_output(data=data)

def make_output(error=None, message=None, data=None):
    if error:
        output = {
            "errors": [
                {
                  "status": "422",
                  "detail": message
                }
            ]
        }
    else:
        output = {
            "data" : data
        }
      
    return json.dumps(output, indent=4)
