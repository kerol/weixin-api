# coding: utf-8
from .base import requests_get, requests_post

# --------------------------------------------------------------------------- #
# 获取二维码
# https://developers.weixin.qq.com/miniprogram/dev/api/qrcode.html
# --------------------------------------------------------------------------- #
def getwxacodeunlimit(access_token, scene, page, width=430, auto_color=None,
        line_color=None, is_hyaline=None):
    """ 接口B：适用于需要的码数量极多的业务场景 """
    api = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token='
    api += access_token
    data = {'scene': scene, 'page': page, 'width': width}
    if auto_color is not None:
        data['auto_color'] = auto_color
    if line_color is not None:
        data['line_color'] = line_color
    if is_hyaline is not None:
        data['is_hyaline'] = is_hyaline

    return requests_post(api, data=data)
