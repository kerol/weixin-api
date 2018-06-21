# coding: utf-8
from .request import requests_get, requests_files

# --------------------------------------------------------------------------- #
# 临时素材接口
# https://developers.weixin.qq.com/miniprogram/dev/api/custommsg/material.html
# --------------------------------------------------------------------------- #


def get(access_token, media_id, **kwargs):
    """ 获取临时素材 """
    api = 'https://api.weixin.qq.com/cgi-bin/media/get'
    params = {'access_token': access_token, 'media_id': media_id}
    params.update(**kwargs)

    return requests_get(api, params)


def upload(access_token, type, media, **kwargs):
    """ 新增临时素材 """
    api = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}'.format(access_token, type)
    files = {'media': media}
    files.update(**kwargs)

    return requests_files(api, files)
