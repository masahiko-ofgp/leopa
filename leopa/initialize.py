import yaml
from pathlib import Path


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
def _create_new_doc(path, filename):
    filepath = path / filename
    filepath.write_text("""
title:
author:
date:

# Heading
""")

# Create new directory
def _create_new_dir(path, dirname):
    new_dir = path / dirname
    new_dir.mkdir()
    return new_dir

def _is_filename(value):
    return isinstance(value, str)

def _is_dir_and_filename(value):
    return isinstance(value, dict)


# Create new project.
class Project:

    def __init__(self, project_name=None):
        self.project_name = project_name
        self.root = Path()

    def create(self):
        if self.project_name is None:
            p = self.root / 'project'
            try:
                p.mkdir()
            except FileExistsError as e:
                print(e)
            else:
                setattr(self, 'config', _create_new_config(p))
                setattr(self, 'docs', _create_new_dir(p, 'docs'))
                print("New project has created!")
        else:
            p = self.root / self.project_name
            try:
                p.mkdir()
            except FileExistsError as e:
                print(e)
            else:
                setattr(self, 'config', _create_new_config(p))
                setattr(self, 'docs', _create_new_dir(p, 'docs'))
                print(f"Your {self.project_name} project has created!")

    def read_config(self):
        if hasattr(self, 'config') is False:
            print("Please create new project.")
        else:
            with open(self.config) as f:
                yml = yaml.safe_load(f)
                return yml

    def read_docs_dir(self):
        config = self.read_config()
        docs = config['docs']
        return docs
