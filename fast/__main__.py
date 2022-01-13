import typer
import os

from pathlib import Path

from fast import fast, __app_name__

app = typer.Typer()


@app.command()
def name():
    fast.name(prog_name=__app_name__)

@app.command()
def createapp():
    typer.echo("create project")
    os.system("cookiecutter https://github.com/jonatasoli/fastapi-template-cookiecutter")
    # typer.launch("./fast/create_app.sh")

if __name__ == "__main__":
    app()
