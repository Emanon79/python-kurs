#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "It is working!"


@app.route("/spider")
def spider():
    return """<!DOCTYPE html>
<html>
<body>
<h1>Spider Testpage</h1>
<p>Hello hello! This is a test page for the spider program.</p>
<p>Here are some emails: hello@spider.com, info@python.org, this_is_me@gmail.com</p>
<p>Here are some links:</p>
<a href="http://localhost/spider1">link1</a>
<a href="http://localhost/spider2">link2</a>
</body>
</html>
    """


@app.route("/spider1")
def spider1():
    return """<!DOCTYPE html>
<html>
<body>
<h1>Spider Testpage1</h1>
<p>Here are some emails: hello1@spider.co.uk, info1@python.org, this_thing@gmail.com</p>
</body>
</html>
    """


@app.route("/spider2")
def spider2():
    return """<!DOCTYPE html>
<html>
<body>
<h1>Spider Testpage1</h1>
<p>Here are some emails: hello2@spider.com, info2@python.org, this_is_me2@gmail.com</p>
</body>
</html>
    """


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
