import urllib.request

url = 'https://pyscript.net/latest/pyscript.js'
try:
    req = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(req, timeout=10) as r:
        print('STATUS', r.status)
except Exception as e:
    print('ERR', repr(e))
