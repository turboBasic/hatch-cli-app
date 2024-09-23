# hatch-cli-app

[Cookiecutter] template for modern Python CLI application project based on Hatch project manager.

[![build](https://github.com/turboBasic/hatch-cli-app/actions/workflows/build.yml/badge.svg?event=push)](https://github.com/turboBasic/hatch-cli-app/actions/workflows/build.yml)


## Features

* Uses [Hatch] - modern PEP-compliant project manager. Project dependencies are described in
PEP-compliant [pyproject.toml] file
* Uses [Typer] framework for managing CLI commands
* Uses [Dynaconf] for flexible management of configurations
* Documentation is built by [mkdocs] and published to GitHub Pages and ReadTheDocs
* [pre-commit] for validation of commits even before they pushed to version control
* GitHub workflows for validation of PRs and published releases
* Publish code coverage reports to [Codecov]
* Publish packages to [PyPI] and [Test PyPI]
* Automatically assign labels to PRs
* Automatically generate Release notes for tagged releases


## Usage

```bash
cookiecutter https://github.com/turboBasic/hatch-cli-app.git
```
Your CLI app is generated in a subdirectory with the name of your project.


## Development

You’re welcome to share your [PRs](https://github.com/turboBasic/hatch-cli-app/pulls) and join
[discussions](https://github.com/turboBasic/hatch-cli-app/discussions).


## Credits

This package is inspired by ideas from [The Hatchlor] project template. The CLI app has been enhanced with
[Dynaconf] package for configuration management.

[Codecov]: https://codecov.io/
[Cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[dynaconf]: https://www.dynaconf.com/
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
[hatch]: https://hatch.pypa.io/
[mkdocs]: https://www.mkdocs.org/
[pipx]: https://pypa.github.io/pipx/
[pre-commit]: https://pre-commit.com/
[pyproject.toml]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[PyPI]: https://pypi.org/
[Test PyPI]: https://test.pypi.org/
[The Hatchlor]: https://github.com/florianwilhelm/the-hatchlor
[Typer]: https://typer.tiangolo.com/
