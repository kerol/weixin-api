# coding: utf-8
from weixin_api.request import requests_get


def access_token(app_id, secret, code):
    """ 通过code换取网页授权access_token """
    api = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    params = {
        'appid': app_id,
        'secret': secret,
        'code': code,
        'grant_type': 'authorization_code',
    }

    return requests_get(api, params)


def refresh_token(app_id, refresh_token):
    """ 刷新access_token """
    api = 'https://api.weixin.qq.com/sns/oauth2/refresh_token'
    params = {
        'appid': app_id,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
    }

    return requests_get(api, params)
