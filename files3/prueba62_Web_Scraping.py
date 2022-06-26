import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112sdfsdfsdas.txt')
print(type(res))

print(res.status_code)
print(requests.codes.ok)

#res.status_code == requests.codes.ok
print(len(res.text))
print(res.text[:250])

try:
    print(res.raise_for_status())
except Exception as exc:
    print('There was a problem: %s' % (exc))