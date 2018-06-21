# coding: utf-8
import traceback
import requests

# --------------------------------------------------------------------------- #
# requests
# --------------------------------------------------------------------------- #

TIMEOUT = 5


def requests_get(url, params, **kwargs):
    kwargs['timeout'] = kwargs.get('timeout', TIMEOUT)
    try:
        res = requests.get(url, params, **kwargs)
        result = False if b'errcode' in res.content[:20] else True
        return result, res
    except Exception:
        print(traceback.print_exc())

    return False, None


def requests_post(url, data, **kwargs):
    kwargs['timeout'] = kwargs.get('timeout', TIMEOUT)
    try:
        res = requests.post(url, json=data, **kwargs)
        result = False if b'errcode' in res.content[:20] else True
        return result, res
    except Exception:
        print(traceback.print_exc())

    return False, None
