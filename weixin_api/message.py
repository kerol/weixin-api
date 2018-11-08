# coding: utf-8
from weixin_api.request import requests_post, requests_get

# --------------------------------------------------------------------------- #
# 客服消息
# https://developers.weixin.qq.com/miniprogram/dev/api/custommsg/conversation.html
# --------------------------------------------------------------------------- #


def custom_send(access_token, data, **kwargs):
    """ 发送客服消息 """
    api = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)
    data.update(**kwargs)

    return requests_post(api, data)


# --------------------------------------------------------------------------- #
# 动态消息
# https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/share/updatable-message.html
# --------------------------------------------------------------------------- #

def wxopen_activityid_create(access_token, params=None, **kwargs):
    """ 创建被分享动态消息的 activity_id """
    api = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/activityid/create?access_token={}'.format(access_token)
    params = {} if not params else params.update(**kwargs)

    return requests_get(api, params)


def wxopen_updatablemsg_send(access_token, activity_id, target_state, template_info, **kwargs):
    """ 发送客服消息 """
    api = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/updatablemsg/send?access_token={}'.format(access_token)
    data = {
        'activity_id': activity_id,
        'target_state': target_state,
        'template_info': template_info,
    }
    data.update(**kwargs)

    return requests_post(api, data)
