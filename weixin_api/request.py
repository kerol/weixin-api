# coding: utf-8
import traceback
import requests

# --------------------------------------------------------------------------- #
# requests
# --------------------------------------------------------------------------- #

TIMEOUT = 3


def _response(methods, url, **kwargs):
    try:
        if methods == 'params':
            res = requests.get(url, kwargs['params'], timeout=TIMEOUT)
        elif methods == 'json':
            res = requests.post(url, json=kwargs['json'], timeout=TIMEOUT)
        elif methods == 'files':
            res = requests.post(url, files=kwargs['files'], timeout=TIMEOUT)
        else:
            return False, None
    except Exception:
        traceback.print_exc()
        return False, None
    try:
        res = res.json()
        result = True if res.get('errcode', 0) == 0 else False
        return result, res
    except Exception:
        return True, res.content


def requests_get(url, params):
    return _response('params', url, params=params)


def requests_post(url, data):
    return _response('json', url, json=data)


def requests_files(url, files):
    return _response('files', url, files=files)
