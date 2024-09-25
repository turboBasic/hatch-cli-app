# hatch-cli-app

[Cookiecutter] template for modern Python CLI application project based on [Hatch] project manager.

[![build status badge]](https://github.com/turboBasic/hatch-cli-app/actions/workflows/build.yml)
<!-- TODO PyPI badge -->


## Goals

- The main goal of [hatch-cli-app] is to have a template for Python CLI project that’s free from outdated
advice that comes up when googling for best practices for Python project.
- I need strongly enforced formatting and linting rules, along with static analysis. However, setting them
up from scratch takes a lot of effort, and it’s a headache to integrate them into existing code after the fact.
- Creating a contributor-friendly internal or public project requires a lot of non-trivial boilerplate code
(workflows, licenses, PR/issue templates, auto-labeling, release notes no name a few). Having this ready to go
without a repeated manual labor is essential. While the release notes part of template isn’t perfect, the
`release-drafter` workflow significantly reduces manual work.
- I don’t use code coverage reports daily, but over time, I’ve found them very helpful for maintaining a
balance between feature development and code quality. Including them in the project ensures I don’t have to
think about setting it up for future projects and get this analytics as a bonus.
- Writing documentation can be tedious, and publishing it for every milestone is even more so. Having the
documentation generated and published automatically is a big advantage for me.
- Finally, publishing packages to PyPI. While this isn’t necessary for internal projects, if you have internal
JFrog or Nexus repositories, adapting the workflow for internal publishing requires minimal changes.


## Features

* Uses [Hatch] - modern PEP-compliant project manager. Project dependencies are described in
PEP-compliant [pyproject.toml] file, generated project uses [ruff], [mypy] and other modern tools
for Python projects
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

Your CLI app is generated in a subdirectory named after your project (`python-cli-app` in the example below,
with non-essential items skipped for brevity):

```plaintext
.
└── python-cli-app
    ├── .editorconfig
    ├── .git
    │   └── <skipped>
    ├── .github
    │   └── <skipped>
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── .readthedocs.yaml
    ├── .secrets.pca.toml.sample
    ├── docs
    │   └── <skipped>
    ├── locks
    ├── mkdocs.yml
    ├── notebooks
    ├── pyproject.toml
    ├── README.md
    ├── settings.pca.toml.sample
    ├── src
    │   └── python_cli_app
    │       ├── __init__.py
    │       ├── cli
    │       │   ├── __init__.py
    │       │   ├── config.py
    │       │   ├── factorial.py
    │       │   ├── fetch.py
    │       │   ├── main.py
    │       │   └── prime.py
    │       ├── config.py
    │       └── defaults
    │           └── settings.pca.toml
    └── tests
        ├── __init__.py
        ├── conftest.py
        ├── test_cli.py
        └── test_cli_config.py
```


## Development

You are welcome to share your [PRs] and join [discussions].


## Credits

This project is inspired by [The Hatchlor] project template. The CLI app has been enhanced with [Dynaconf]
package for management of public and secret configurations, extracting commands into separate modules,
supporting both simple commands and commands with subcommands.

Additionally, workflows have been enhanced to include code coverage reports, publishing of documentation
to GitHub Pages and [Read the Docs], as well as distinguishing development and production releases, which
are published to [Test PyPI] and [PyPI] respectively.

[SSW.GitHub.Template] by SSWConsulting was used as an inspiration for issue and PR templates. I also
strongly recommend reading their [44 Rules to Better Github] if you’re aiming to create a user- and
contributor-friendly experience for your GitHub projects.


<!-- External links -->
[44 Rules to Better Github]: https://www.ssw.com.au/rules/rules-to-better-github/
[Codecov]: https://codecov.io/
[Cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[dynaconf]: https://www.dynaconf.com/
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
[hatch]: https://hatch.pypa.io/
[mkdocs]: https://www.mkdocs.org/
[mypy]: https://mypy-lang.org/
[pipx]: https://pypa.github.io/pipx/
[pre-commit]: https://pre-commit.com/
[pyproject.toml]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[PyPI]: https://pypi.org/
[Read the Docs]: https://readthedocs.org/
[ruff]: https://docs.astral.sh/ruff/
[SSW.GitHub.Template]: https://github.com/SSWConsulting/SSW.GitHub.Template
[Test PyPI]: https://test.pypi.org/
[The Hatchlor]: https://github.com/florianwilhelm/the-hatchlor
[Typer]: https://typer.tiangolo.com/

<!-- Project links -->
[build status badge]:https://github.com/turboBasic/hatch-cli-app/actions/workflows/build.yml/badge.svg?event=push
[discussions]: https://github.com/turboBasic/hatch-cli-app/discussions
[hatch-cli-app]: https://github.com/turboBasic/hatch-cli-app
[PRs]: https://github.com/turboBasic/hatch-cli-app/pulls
