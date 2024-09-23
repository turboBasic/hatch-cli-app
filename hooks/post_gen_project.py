import subprocess

try:
    subprocess.call(['git', 'init', '--initial-branch', 'main'])
    subprocess.call(['git', 'commit', '--allow-empty', '-m', 'chore: root commit'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'feat!: expand cookiecutter template'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_repo }}'])
    print('Follow-up all TODO items inserted as comments in generated code')
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print("Please ensure that you manually establish a Git repository")
