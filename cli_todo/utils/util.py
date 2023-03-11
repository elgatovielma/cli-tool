from urllib import request, parse
from urllib.error import HTTPError

import random
import lorem

    
def create_random_todos():
    """
        create random number of todos between 10 and 100
    """
    random_number = random.randint(10, 100)
    for i in range(random_number):
        todo = lorem.sentence()
        data = http_handler("POST", text=todo)
    return data


def delete_all_todos(todos):
    """
        delete all todos
    """
    for todo in todos:
        data = http_handler("DELETE", id=todo["_id"])
    return data
    
        

def http_handler(method, text=None, id=None):
    """
        Http handler to execute queries
    """
    # Define the URL to make the request to
    url = "http://localhost:8080/api/todos"
    try:
        # Make request depending in the method
        if method == "GET":
            req = request.Request(url)
        elif method == "POST":
            data = parse.urlencode({"text": text}).encode()
            req = request.Request(url, data=data)
        elif method == "DELETE":
            url =  f'{url}/{id}'
            req = request.Request(url, method="DELETE")
        # Read the response and decode 
        response = request.urlopen(req)
    except HTTPError as e:
        print("HTTP error occurred:", e.code)
    except Exception as e:
        print("Error occurred:", e)
    else:
        # Decode and return response
        if response.getcode() == 200:
            source = response.read()
            return source