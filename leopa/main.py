import yaml
from pathlib import Path
from .template import MARKDOWN_TPL, create_html


# Create config.yaml
def _create_new_config(path):
    confpath = path / 'config.yaml'
    confpath.write_text('''\
site_name: "Your site name"
site_url: "https://example.com"
site_description: "brah brah brah..."
site_author: "author name"
copyright: "Copyright (c) ...."
docs:
    - "index.md"
''')
    return confpath

# Create new markdown document
def _create_new_doc(path, filename, suffix=False):
    filepath = path / filename

    if suffix is False:
        filepath.write_text(MARKDOWN_TPL)
    else:
        f2 = filepath.stem + ".html"
        new_file_path = path / f2
        new_file_path.write_text("")

# Create new directory
def _create_new_dir(path, dirname):
    new_dir = path / dirname
    new_dir.mkdir()
    return new_dir

def _rec_create_tree(path, dirname, suffix=False):
    for d in dirname:
        if isinstance(d, str):
            _create_new_doc(path, d, suffix)
        elif isinstance(d, dict):
            for k, v in d.items():
                if isinstance(v, list):
                    d2 = _create_new_dir(path, k)
                    _rec_create_tree(d2, v, suffix)
                else:
                    d2 = _create_new_dir(path, k)
                    _create_new_doc(d2, v, suffix)
        else:
            break


# Create new project.
class Project:

    def __init__(self, project_name=None):
        self.project_name = project_name
        self.current = Path()

    def create(self):
        if self.project_name is None:
            p = self.current / 'project'
            setattr(self, 'root', p)
            try:
                p.mkdir()
            except FileExistsError as e:
                print(e)
            else:
                setattr(self, 'config', _create_new_config(p))
                setattr(self, 'docs', _create_new_dir(p, 'docs'))
                setattr(self, 'public', _create_new_dir(p, 'public'))
                print("New project has created!")
        else:
            p = self.current / self.project_name
            setattr(self, 'root', p)
            try:
                p.mkdir()
            except FileExistsError as e:
                print(e)
            else:
                setattr(self, 'config', _create_new_config(p))
                setattr(self, 'docs', _create_new_dir(p, 'docs'))
                setattr(self, 'public', _create_new_dir(p, 'public'))
                print(f"Your {self.project_name} project has created!")

    def read_config(self):
        if hasattr(self, 'config') is False:
            print("Please create new project.")
        else:
            with open(self.config) as f:
                yml = yaml.safe_load(f)
                return yml

    def reload(self):
        config = self.read_config()
        docs = config['docs']
        _rec_create_tree(Path(self.docs), docs)

    def publish(self):
        config = self.read_config()
        docs = config['docs']
        _rec_create_tree(Path(self.public), docs, suffix=True)
