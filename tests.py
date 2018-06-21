# coding: utf-8
import weixin_api

access_token = '123'

if __name__ == '__main__':
    print(weixin_api.auth.access_token('123', '123'))
    print(weixin_api.auth.jscode2session('', '', ''))

    print(weixin_api.media.get(access_token, ''))
    print(weixin_api.media.upload(access_token, '', ''))

    print(weixin_api.message.custom_send(access_token, {}))

    print(weixin_api.qrcode.getwxacode(access_token, ''))
    print(weixin_api.qrcode.getwxacodeunlimit(access_token, ''))
    print(weixin_api.qrcode.createwxaqrcode(access_token, ''))

    print(weixin_api.template.library_list(access_token, '', ''))
    print(weixin_api.template.library_get(access_token, ''))
    print(weixin_api.template.add(access_token, '', ''))
    print(weixin_api.template.list(access_token, '', ''))
    print(weixin_api.template.delete(access_token, ''))
    print(weixin_api.template.send(access_token, '', ''))
