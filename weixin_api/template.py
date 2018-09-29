# coding: utf-8
from weixin_api.request import requests_post

# --------------------------------------------------------------------------- #
# 模版消息
# https://developers.weixin.qq.com/miniprogram/dev/api/notice.html
# --------------------------------------------------------------------------- #


def library_list(access_token, offset, count, **kwargs):
    """ 获取小程序模板库标题列表 """
    api = 'https://api.weixin.qq.com/cgi-bin/wxopen/template/library/list?access_token={}'.format(access_token)
    data = {'offset': offset, 'count': count}
    data.update(**kwargs)

    return requests_post(api, data)


def library_get(access_token, title_id, **kwargs):
    """ 获取模板库某个模板标题下关键词库 """
    api = 'https://api.weixin.qq.com/cgi-bin/wxopen/template/library/get?access_token={}'.format(access_token)
    data = {'id': title_id}
    data.update(**kwargs)

    return requests_post(api, data)


def add(access_token, title_id, keyword_id_list, **kwargs):
    """ 组合模板并添加至帐号下的个人模板库 """
    api = 'https://api.weixin.qq.com/cgi-bin/wxopen/template/add?access_token={}'.format(access_token)
    data = {'id': title_id, 'keyword_id_list': keyword_id_list}
    data.update(**kwargs)

    return requests_post(api, data)


def list(access_token, offset, count, **kwargs):
    """ 获取帐号下已存在的模板列表 """
    api = 'https://api.weixin.qq.com/cgi-bin/wxopen/template/list?access_token={}'.format(access_token)
    data = {'offset': offset, 'count': count}
    data.update(**kwargs)

    return requests_post(api, data)


def delete(access_token, template_id, **kwargs):
    """ 删除帐号下的某个模板 """
    api = 'https://api.weixin.qq.com/cgi-bin/wxopen/template/del?access_token={}'.format(access_token)
    data = {'template_id': template_id}
    data.update(**kwargs)

    return requests_post(api, data)


def send(access_token, touser, template_id, **kwargs):
    """ 发送模板消息 """
    api = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}'.format(access_token)
    data = {'touser': touser, 'template_id': template_id}
    data.update(**kwargs)

    return requests_post(api, data)
