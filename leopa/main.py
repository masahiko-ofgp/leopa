import yaml
try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import Loader

from pathlib import Path
from .template import MARKDOWN_TPL, convert_md


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
def _create_new_doc(path, filename, content, suffix=False):
    filepath = path / filename

    if suffix is False:
        filepath.write_text(content)
    else:
        filename = filepath.stem + ".html"
        f2 = path / filename
        f2.write_text(content)

# Create new directory
def _create_new_dir(path, dirname):
    new_dir = path / dirname
    new_dir.mkdir()
    return new_dir

def _rec_create_tree(path, dirname, content, suffix=False):
    for d in dirname:
        if isinstance(d, str):
            _create_new_doc(path, d, content, suffix)
        elif isinstance(d, dict):
            for k, v in d.items():
                if isinstance(v, list):
                    d2 = _create_new_dir(path, k)
                    _rec_create_tree(d2, v, content, suffix)
                else:
                    d2 = _create_new_dir(path, k)
                    _create_new_doc(d2, v, content, suffix)
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
                yml = yaml.load(f, Loader=Loader)
                return yml

    def reload(self):
        config = self.read_config()
        docs = config['docs']
        _rec_create_tree(Path(self.docs), docs, MARKDOWN_TPL)

    def publish(self):
        config = self.read_config()
        docs = Path(self.docs)
        docs_files = []
        for d in docs.rglob("*.md"):
            docs_files.append("./" + str(d))
        
        for d in docs_files:
            content = convert_md(d, config['site_name'])
            _rec_create_tree(
                    Path(self.public),
                    docs_files,
                    content,
                    suffix=True
                )

