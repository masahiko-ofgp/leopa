# Leopa

<img src="./imgs/leopa.png" width=60% alt="leopa-logo">

Static site generator with Python3.

## Usage

```
>>> import leopa
>>> p = leopa.Project()
>>> p.create()
New project has created!
>>> # If you want to add some new doc,
>>> #  you edit config.yaml.
>>> # then you do as follows.
>>> p.reload()
>>> # If you want to create html files,
>>> # you do as follows.
>>> p.publish()
```
