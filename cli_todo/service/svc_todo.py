from cli_todo.utils import util


class Todo:
    """
        This class represents the todo
    """
    
    def __init__(self):
        pass
    
    
    def get_all_todos(self):
        """
            Http call to get all todos
        """
        return util.http_handler(method="GET")
            
            
    def create_todo(self, text):
        """
            Http call to create a todos
        """
        return util.http_handler(method="POST", text=text)
            
    
    def delete_todo(self, id):
        """
            Http call to delete a todo
        """
        return util.http_handler(method="DELETE", id=id)