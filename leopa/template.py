from string import Template
#title,description,author,keyword,css_url,site_name,content,copyright

MARKDOWN_TPL = '''\
title:
author:
date:

# Headind

brahbrahbrah...
'''

BASE_TPL = Template('''\
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <meta name="description" content="${description}">
    <meta name="author" content="${author}">
    <meta name="keyword" content="${keywoord}">
    <link rel="stylesheet" href="${css_url}" type="text/css">
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

def create_html(title, description, author, keyword, css_url, site_name,
        content, copyright):
    html = BASE_TPL.safe_substitute(
            title=title,
            description=description,
            author=author,
            keyword=keyword,
            css_url=css_url,
            site_name=site_name,
            content=content,
            copyright=copyright
            )
    return html
