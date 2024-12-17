from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)
html_doc="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

@app.route('/', methods=['GET','POST'])
def soup():
    if request.method=='POST':
        link_ls=[]
        soup = BeautifulSoup(html_doc, 'html.parser')
        for link in soup.find_all('a'):
            link_ls.append(link.get('href'))
        return render_template('Parser.html', link=link_ls)
    return render_template('Parser.html')

if __name__ == '__main__':
    app.run()