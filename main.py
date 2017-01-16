from mistune import Markdown
import premailer
import os


def pack_html(html):
    top = """<!DOCTYPE html><html lang="zh-cn">
          <head>
          <meta charset="UTF-8">
          <title>output</title>
          <link rel="stylesheet" type="text/css" href="style.css">
          </head>
          <body>"""

    bottom = """</body></html>"""
    return top + html + bottom

if __name__ == '__main__':

    for file in os.listdir('temp'):

        if file.endswith('.md'):
            with open('temp/{fn}'.format(fn=file), 'r', encoding='utf-8') as mdfile:
                mdstr = mdfile.read()

            md = Markdown()
            raw_html = md(mdstr)
            result = premailer.transform(pack_html(raw_html))

            with open('temp/{fn}.html'.format(fn=file[:-3]),
                      'w', encoding='utf-8') as htmlfile:
                htmlfile.write(result)




