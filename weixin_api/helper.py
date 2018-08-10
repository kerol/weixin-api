# coding: utf-8
import hashlib
import hmac


def sorted_str(params):
    """ 按照字典ASCII升序 """
    return '&'.join(['{}={}'.format(str(k), str(params[k])) for k in sorted(params)])


def hmac_sha256(key, sign_str):
    hash = hmac.new(key.encode(), sign_str.encode(), hashlib.sha256)
    return hash.hexdigest()
