# coding: utf-8
from weixin_api.request import requests_post

# --------------------------------------------------------------------------- #
# 客服消息
# https://developers.weixin.qq.com/miniprogram/dev/api/custommsg/conversation.html
# --------------------------------------------------------------------------- #


def custom_send(access_token, data, **kwargs):
    """ 发送客服消息 """
    api = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)
    data.update(**kwargs)

    return requests_post(api, data)
