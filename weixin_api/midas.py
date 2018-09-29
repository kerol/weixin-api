# coding: utf-8
import time

from weixin_api.request import requests_post
from weixin_api.helper import sorted_str, hmac_sha256

# --------------------------------------------------------------------------- #
# 米大师
# https://developers.weixin.qq.com/minigame/dev/tutorial/open-ability/payment.html
# --------------------------------------------------------------------------- #

class MidasPay:
    """ 微信米大师虚拟支付 """

    def __init__(self, app_id, zone_id='1', offer_id='', pf='android', sandbox=False, app_key=''):
        self.sandbox = sandbox
        self.app_key = app_key
        self.common_params = {
            'appid': app_id,
            'offer_id': offer_id,
            'zone_id': zone_id,
            'pf': pf,
        }

    def encrypt(self, access_token, session_key, method, path, params):
        """ 加密 """
        # sig
        sign_str = sorted_str(params)
        sign_str += '&org_loc={}&method={}&secret={}'.format(path, method.upper(), self.app_key)
        sig = hmac_sha256(self.app_key, sign_str)
        params['sig'] = sig
        params['access_token'] = access_token
        # mp_sig
        sign_str = sorted_str(params)
        sign_str += '&org_loc={}&method={}&session_key={}'.format(path, method.upper(), session_key)
        mp_sig = hmac_sha256(session_key, sign_str)
        params['mp_sig'] = mp_sig

        del params['access_token']

        return params

    def build_params(self, access_token, session_key, params, path, **kwargs):
        """ 构造参数 """
        params.update(**kwargs)
        params.update(self.common_params)
        params['ts'] = int(time.time())

        return self.encrypt(access_token, session_key, 'POST', path, params)

    def getbalance(self, access_token, session_key, open_id, **kwargs):
        """
        查询余额: 查看某个用户的游戏币余额
        """
        path = '/cgi-bin/midas/sandbox/getbalance' if self.sandbox else '/cgi-bin/midas/getbalance'
        api = 'https://api.weixin.qq.com{}?access_token={}'.format(path, access_token)
        params = {'openid': open_id}
        data = self.build_params(access_token, session_key, params, path, **kwargs)

        return requests_post(api, data)

    def pay(self, access_token, session_key, open_id, bill_no, amount, **kwargs):
        """
        扣除游戏币: 扣除某个用户的游戏币
        """
        path = '/cgi-bin/midas/sandbox/pay' if self.sandbox else '/cgi-bin/midas/pay'
        api = 'https://api.weixin.qq.com{}?access_token={}'.format(path, access_token)
        params = {
            'openid': open_id,
            'amt': amount,
            'bill_no': bill_no,
        }
        data = self.build_params(access_token, session_key, params, path, **kwargs)

        return requests_post(api, data)

    def cancelpay(self, access_token, session_key, open_id, bill_no, **kwargs):
        """
        取消支付: 在有效期内的订单，可以通过本接口取消该笔扣除游戏币的订单
        """
        path = '/cgi-bin/midas/sandbox/cancelpay' if self.sandbox else '/cgi-bin/midas/cancelpay'
        api = 'https://api.weixin.qq.com{}?access_token={}'.format(path, access_token)
        params = {
            'openid': open_id,
            'bill_no': bill_no,
        }
        data = self.build_params(access_token, session_key, params, path, **kwargs)

        return requests_post(api, data)

    def present(self, access_token, session_key, open_id, bill_no, present_counts, **kwargs):
        """
        游戏币赠送: 向某个用户赠送游戏币
        """
        path = '/cgi-bin/midas/sandbox/present' if self.sandbox else '/cgi-bin/midas/present'
        api = 'https://api.weixin.qq.com{}?access_token={}'.format(path, access_token)
        params = {
            'openid': open_id,
            'bill_no': bill_no,
            'present_counts': present_counts,
        }
        data = self.build_params(access_token, session_key, params, path, **kwargs)

        return requests_post(api, data)
