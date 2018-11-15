import urllib.request
with urllib.request.urlopen('https://1drv.ms/f/s!AtOQ3zkxCmbZg0-JN_fp7hLStEKY') as response:
    html = response.read()

app_secret = 'wxcfnRUHV692=_@hxFZD55='

print(html)