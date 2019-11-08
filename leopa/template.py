from markdown import Markdown
from string import Template


MARKDOWN_TPL = '''\
title:
description:
author:
date:
keyword:
css:

# Heading

blahblahblah...
'''

def convert_md(filename, site_name):
    m = Markdown(extensions=['meta'])

    with open(filename, 'rt', encoding='utf-8') as f:
        text = f.read()
        content = m.convert(text)
        metadata = m.Meta
    
    html = create_html(
            metadata['title'][0],
            metadata['description'][0],
            metadata['author'][0],
            metadata['date'][0],
            ', '.join(metadata['keyword']),
            metadata['css'][0],
            site_name,
            content,
            site_name + ' ' + metadata['author'][0]
                )
    return html


_BASE_TPL = Template('''\
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <meta name="description" content="${description}">
    <meta name="author" content="${author}">
    <meta name="date" content="${date}">
    <meta name="keyword" content="${keyword}">
    <link rel="stylesheet" href="${css}" type="text/css">
  </head>
  <body>
    <header>
      <h1>${site_name}</h1>
    </header>
    <article>
      ${content}
    </article>
    <footer>
      <span>Copyright (c) ${copyright} </span>
    </footer>
  </body>
<html>
''')

def create_html(title, description, author, date, keyword, css,
        site_name, content, copyright):
    html = _BASE_TPL.safe_substitute(
            title=title,
            description=description,
            author=author,
            date=date,
            keyword=keyword,
            css=css,
            site_name=site_name,
            content=content,
            copyright=copyright
            )
    return html
