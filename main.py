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

def convert_all():
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
                print("成功：转换后的.html文件保存在temp文件夹中")

if __name__ == '__main__':
    try:
        convert_all()
    except:
        input("错误：运行前请将所有要转换的.md文件放入temp文件夹中\n"
              "按回车键结束程序：")






