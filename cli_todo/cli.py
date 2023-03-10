from cli_todo.service import svc_todo
from cli_todo.utils import util

import click
import json
from prettytable import PrettyTable

class Context:
    def __init__(self):
        self.todo = svc_todo.Todo()


@click.group()
@click.pass_context
def cli(ctx):
    """
        Welcome to Todo cli tool! 
        An all-in-one cli utility tool to get your todos!
    """
    ctx.obj = Context()
     

@cli.command(
    help="Execute get command. Argument: --format "
)
@click.pass_context
@click.option(
    "-f", 
    "--format", 
    type=str, 
    help="Get all todos in different formats using the argument format and value: json, txt or table", 
    default="json", 
    show_default=True
)
def get(ctx, format):
    try:
        data = json.loads(ctx.obj.todo.get_all_todos())
    except ValueError as e:
        print("Error parsing JSON data:", e)
    else:
        if format == "json":
            click.echo(json.dumps(data, indent=4, sort_keys=True))
        elif format == "txt":
            click.echo(data)
        elif format == "table":
            # PrettyTable allows us to print the info in a nice tabular way
            headers = ["id", "v", "text"]
            myTable = PrettyTable(headers)
            for element in data:
                myTable.add_row(element.values())
            click.echo(myTable)
        else: 
            click.echo("No valid value")
            
            
@cli.command(
    help="Execute insert command. Argument: --text "
)
@click.pass_context
@click.option(
    "-t", 
    "--text", 
    type=str,
    default="", 
    help="Insert a whole new todo to your list of todos using the argument text and as value your todo"
)
def insert(ctx, text):
    if text == "":
        click.echo("please use the argument text")
        return 
    try:
        data = json.loads(ctx.obj.todo.create_todo(text))
    except ValueError as e:
        print("Error parsing JSON data:", e)
    else:
        click.echo(data)
        
        
@cli.command(
    help="Execute delete command. Argument: --id "
)
@click.pass_context
@click.option(
    "--id", 
    type=str,
    default="", 
    help="Delete a todo from your list using the argument id and as value that id"
)
def delete(ctx, id):
    if id == "":
        click.echo("please use the argument id")
        return 
    try:
        data = json.loads(ctx.obj.todo.delete_todo(id))
    except ValueError as e:
        print("Error parsing JSON data:", e)
    else:
        click.echo(data)
        
        
@cli.command(
    help="Execute workflow challenge"
)
def workflow():
    try:
        data = json.loads(util.create_random_todos())
    except ValueError as e:
        print("Error parsing JSON data:", e)
    else:
        click.echo(json.dumps(data, indent=4, sort_keys=True))
        click.echo(data)
        # PrettyTable allows us to print the info in a nice tabular way
        headers = ["id", "v", "text"]
        myTable = PrettyTable(headers)
        for element in data:
            myTable.add_row(element.values())
        click.echo(myTable)
        util.delete_all_todos(data)
    
    
    
        
        
        
