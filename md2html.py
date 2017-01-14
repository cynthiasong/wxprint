from mistune import Markdown

md = Markdown()

def pack_html(html):
    top = """<!DOCTYPE html><html lang="zh-cn">
          <head>
          <meta charset="UTF-8">
          <title>output</title>
          <link rel="stylesheet" type="text/css" href="../style.css">
          </head>
          <body>"""

    bottom = """</body></html>"""
    return top + html + bottom

with open('temp/test.md', 'r', encoding='utf-8') as mdfile:
    test = mdfile.read()

with open('temp/test.html', 'w', encoding='utf-8') as htmlfile:
    result = md(test)
    htmlfile.write(pack_html(result))

# print(pack_html(result))


