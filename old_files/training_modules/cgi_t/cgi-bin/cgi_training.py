#!/usr/bin/env python3
import cgi
import html
import http.cookies
import os

form = cgi.FieldStorage()
name = html.escape(form.getfirst('name', 'None'))
age = html.escape(form.getfirst('age', 'None'))

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
if name == 'None':
    name = cookie.get("name").value

print("Content-type: text/html\n")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Result</title>
</head>
<body>""")

print("<h1>Result</h1>")
print("<p>Name: {}</p>".format(name))
print("<p>Age: {}</p>".format(age))

print("""</body>
</html>""")