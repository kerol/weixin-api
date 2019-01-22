# coding: utf-8
import traceback
import requests
import ujson as json

# --------------------------------------------------------------------------- #
# requests
# --------------------------------------------------------------------------- #

TIMEOUT = 3


def _response(methods, url, **kwargs):
    try:
        if methods == 'params':
            res = requests.get(url, kwargs['params'], timeout=TIMEOUT)
        elif methods == 'data':
            res = requests.post(url, data=kwargs['data'], timeout=TIMEOUT)
        elif methods == 'files':
            res = requests.post(url, files=kwargs['files'], timeout=TIMEOUT)
        else:
            return False, None
    except Exception:
        traceback.print_exc()
        return False, None
    try:
        res.encoding = 'utf-8'
        res = res.json()
        result = True if res.get('errcode', 0) == 0 else False
        return result, res
    except Exception:
        return True, res.content


def requests_get(url, params):
    return _response('params', url, params=params)


def requests_post(url, data):
    data = json.dumps(data, ensure_ascii=False)
    data = data.encode('utf8')
    return _response('data', url, data=data)


def requests_files(url, files):
    return _response('files', url, files=files)
