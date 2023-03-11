# How to run todo app
Open a terminal and make sure your current directory is the same where you have the **docker-compose.yml** file and you have docker install.
Then run the following command to start the application:
```bash
docker-compose up
```

# How to install todo app cli tool

Make sure you have Python 3 and pip3 install
Then run the following command to install the application cli tool package:
```bash
pip install git+https://github.com/elgatovielma/cli-tool.git
```
or
```bash
pip3 install git+https://github.com/elgatovielma/cli-tool.git
```

now you will have installed the todo command tool. You can test it:
```bash
$ todo
Usage: todo [OPTIONS] COMMAND [ARGS]...

  Welcome to Todo cli tool!  An all-in-one cli utility tool to get your
  todos!

Options:
  --help  Show this message and exit.

Commands:
  delete    Execute delete command Argument: --id
  get       Execute get command Argument: --format
  insert    Execute insert command Argument: --text
  workflow  Execute workflow challenge
```

# Example commands

Get todos in tabular format:
```bash
todo get --format table
```

Insert new todo:
```bash
todo insert --text "<value>"
```

Delete todo:
```bash
todo delete --id <value>
```

Workflow challenge:
```bash
todo workflow
```

### Enjoy the todos!

P.S: The dockerfile is to show how I built the docker image to containerize the [todo app](https://github.com/scotch-io/node-todo)

