# coding: utf-8
import traceback
import base64
import ujson as json
from Crypto.Cipher import AES

from .request import requests_get


def access_token(app_id, secret):
    api = 'https://api.weixin.qq.com/cgi-bin/token'
    params = {
        'appid': app_id,
        'secret': secret,
        'grant_type': 'client_credential',
    }

    return requests_get(api, params)


def jscode2session(app_id, secret, js_code):
    """ 临时登录凭证校验接口 """
    api = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': app_id,
        'secret': secret,
        'js_code': js_code,
        'grant_type': 'authorization_code',
    }

    return requests_get(api, params)


def decrypt(session_key, encrypted_data, iv, app_id):
    """ 解密用户数据 """
    session_key = base64.b64decode(session_key)
    encrypted_data = base64.b64decode(encrypted_data)
    iv = base64.b64decode(iv)

    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    ret = _unpad(cipher.decrypt(encrypted_data))
    try:
        decrypted = json.loads(ret)
        if decrypted['watermark']['appid'] == app_id:
            return decrypted
    except Exception:
        traceback.print_exc()
