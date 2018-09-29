# coding: utf-8
from weixin_api.request import requests_post

# --------------------------------------------------------------------------- #
# 获取二维码
# https://developers.weixin.qq.com/miniprogram/dev/api/qrcode.html
# --------------------------------------------------------------------------- #


def getwxacode(access_token, path, **kwargs):
    """ 接口A: 适用于需要的码数量较少的业务场景 """
    api = 'https://api.weixin.qq.com/wxa/getwxacode?access_token={}'.format(access_token)
    data = {'path': path}
    data.update(**kwargs)

    return requests_post(api, data)


def getwxacodeunlimit(access_token, scene, **kwargs):
    """ 接口B：适用于需要的码数量极多的业务场景 """
    api = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={}'.format(access_token)
    data = {'scene': scene}
    data.update(**kwargs)

    return requests_post(api, data)


def createwxaqrcode(access_token, path, **kwargs):
    """ 接口C：适用于需要的码数量较少的业务场景 """
    api = 'https://api.weixin.qq.com/cgi-bin/wxaapp/createwxaqrcode?access_token={}'.format(access_token)
    data = {'path': path}
    data.update(**kwargs)

    return requests_post(api, data)