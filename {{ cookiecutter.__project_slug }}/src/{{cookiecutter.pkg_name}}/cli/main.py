"""
Creates CLI commands and sub-commands using [Typer](https://typer.tiangolo.com) package.

This module can be invoked from shell by executing `{{ cookiecutter.cli_command_name }}` command. This is
enabled in the following lines in `pyproject.toml`:

```toml
[project.scripts]
{{ cookiecutter.cli_command_name }} = "{{ cookiecutter.pkg_name }}.cli.main:app"
```

Read detailed help about commands and parameters by executing `{{ cookiecutter.cli_command_name }} --help`
"""

import logging
from typing import Annotated

import typer

from {{ cookiecutter.pkg_name }} import __version__
from {{ cookiecutter.pkg_name }}.cli import config, factorial, fetch, prime
from {{ cookiecutter.pkg_name }}.config import load_config_file

app = typer.Typer(help=f'{{ cookiecutter.project_short_description }}. Version: {__version__}')

# Inject `config` and `fetch` as subcommands which in turn can have its own subcommands
app.add_typer(config.app, name='config')
app.add_typer(fetch.app, name='fetch')

# Because cli.prime and cli.factorial do not have subcommands, we inject them directly
# as commands, not as a sub-typer (see https://github.com/fastapi/typer/issues/119)
app.command(name='factorial')(factorial.main)
app.command(name='prime')(prime.main)


def version_callback(value: bool):  # noqa: FBT001
    if value:
        typer.echo(f'{{ cookiecutter.project_name }}: {__version__}')
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    config_file: Annotated[list[str] | None, typer.Option(help='Config file')] = None,
    version: Annotated[
        bool | None,
        typer.Option('--version', callback=version_callback, is_eager=True),
    ] = None,
):
    """{{ cookiecutter.project_short_description }} template: boilerplate project for modern CLI utility"""
    logging.getLogger(__name__).debug(f'Global arguments: config-file={config_file}, version={version}')
    for config_file_item in config_file or []:
        load_config_file(config_file_item)
    logging.getLogger(__name__).debug(f'About to execute command: {ctx.invoked_subcommand}')


if __name__ == '__main__':
    app()
