import json
from flask.cli import FlaskGroup
from project import app, routes


cli = FlaskGroup(app)


def user_input():
    """Command description and Getting user input"""
    return input("\n\nPlease write the page you would like to output \n"
                 "possible pages are: \nindex \npersonal \nexperience \neducation \n"
                 "to quit write q, quit, exit or e\n: ")


@cli.command("output_cv")
def output_cv():
    """Function returning json response based on user input"""
    quit_options = ['q', 'quit', 'exit', 'e']
    while True:
        while True:
            u_input = user_input().lower()
            if u_input in quit_options:
                return False
            output, status = routes.media_status_loader(u_input)
            if status == 200:
                print(json.dumps(output, indent=2, sort_keys=False))
            else:
                print("Incorrect output value, try again\n\n")
                continue


if __name__ == "__main__":
    cli()
