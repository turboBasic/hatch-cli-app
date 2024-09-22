# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

<!-- TODO Enable and configure your workflows -->
[![build]({{ cookiecutter.project_repo }}/actions/workflows/build.yml/badge.svg?event=push)]({{ cookiecutter.project_repo }}/actions/workflows/build.yml)
<!-- TODO Replace <INSERT_TOKEN_FROM_COVERAGE_IO> string with actual token for your project in Coverage.io -->
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug }}/graph/badge.svg?token=<INSERT_TOKEN_FROM_COVERAGE_IO>)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug }})

![{{ cookiecutter.pkg_name }}-template logo](https://raw.githubusercontent.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug }}/refs/heads/main/docs/assets/images/favicon.svg)


## Features

* Uses [Hatch] - modern PEP-compliant project manager
* Uses [Typer] framework for managing CLI commands
* Uses [Dynaconf] for flexible management of configurations

## Usage

```bash
{{ cookiecutter.cli_command_name }}  --help
```

## Development

To set up [hatch] and [pre-commit] for the first time:

1. install [hatch] globally, e.g. with [pipx] or brew, i.e. `pipx install hatch`,
2. make sure [pre-commit] is installed globally, e.g. with `pipx install pre-commit`.

A special feature that makes hatch very different from other familiar tools is that you almost never
activate, or enter, an environment. Instead, you use `hatch run env_name:command` and the `default` environment
is assumed for a command if there is no colon found. Thus you must always define your environment in a declarative
way and hatch makes sure that the environment reflects your declaration by updating it whenever you issue
a `hatch run ...`. This helps with reproducability and avoids forgetting to specify dependencies since the
hatch workflow is to specify everything directly in [pyproject.toml]. Only in rare cases, you
will use `hatch shell` to enter the `default` environment, which is similar to what you may know from other tools.

To get you started, use `hatch run test:cov` or `hatch run test:no-cov` to run the unitest with or without coverage reports,
respectively. Use `hatch run lint:all` to run all kinds of typing and linting checks. Try to automatically fix linting
problems with `hatch run lint:fix` and use `hatch run docs:serve` to build and serve your documentation.
You can also easily define your own environments and commands. Check out the environment setup of hatch
in [pyproject.toml] for more commands as well as the package, build and tool configuration.

The environments defined by hatch are configured to generate lock files using [hatch-pip-compile] under `locks`.
To upgrade all packages in an environment like `test`, just run `hatch run test:upgrade-all`. To upgrade specific
packages, type `hatch run test:upgrade-pkg pkg1,pkg2`.

## Credits

This package was created with [Hatch CLI App] project template.

[dynaconf]: https://www.dynaconf.com/
[Hatch CLI App]: https://github.com/turboBasic/hatch-cli-app
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
[hatch]: https://hatch.pypa.io/
[mypy]: https://mypy-lang.org/
[pipx]: https://pypa.github.io/pipx/
[pre-commit]: https://pre-commit.com/
[pyproject.toml]: {{ cookiecutter.project_repo }}/blob/main/pyproject.toml
[ruff]: https://docs.astral.sh/ruff/
[Typer]: https://typer.tiangolo.com/
