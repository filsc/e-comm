from app import create_app, cli
from app.cli import blueprint
#from app import app

app = create_app()
app.cli.add_command(blueprint)

@app.shell_context_processor
def makeShellContext():
    return dict()



