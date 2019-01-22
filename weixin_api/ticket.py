# coding: utf-8
from weixin_api.request import requests_get

# --------------------------------------------------------------------------- #
# api_ticket
# --------------------------------------------------------------------------- #


def getticket(access_token, params=None, **kwargs):
    """ 获取api_ticket """
    api = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=wx_card'.format(access_token)
    params = {} if not params else params.update(**kwargs)

    return requests_get(api, params)
