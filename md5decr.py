import requests

def tr(hash):
    url='http://www.nitrxgen.net/md5db/'+hash
    r=requests.get(url)
    if r.text=='':
        return "I couldn't find this hash."
    else:
        decr=r.text
        return decr
