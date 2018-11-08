# coding: utf-8
from weixin_api.request import requests_get

from . import oauth2


def userinfo(access_token, openid):
    """ 拉取用户信息 """
    api = 'https://api.weixin.qq.com/sns/userinfo'
    params = {
        'access_token': access_token,
        'openid': openid,
    }

    return requests_get(api, params)


def auth(access_token, openid):
    """ 检验授权凭证（access_token）是否有效 """
    api = 'https://api.weixin.qq.com/sns/auth'
    params = {
        'access_token': access_token,
        'openid': openid,
    }

    return requests_get(api, params)
