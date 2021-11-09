import urllib.request as urllibr

web = urllibr.urlopen('https://google.com')

print(str(web.getcode()))

data = web.read()
print(data)

enc = web.info().get_content_charset()
html = data.decode(enc)

print(enc)
print(html)