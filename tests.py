# coding: utf-8
access_token = ''

# --------------------------------------------------------------------------- #
# 测试获取二维码
# --------------------------------------------------------------------------- #
def test_getwxacodeunlimit():
    from weixin_api.wxa import getwxacodeunlimit
    result, res = getwxacodeunlimit(access_token, '123', '')
    print(result, res.content)


if __name__ == '__main__':
    test_getwxacodeunlimit()
