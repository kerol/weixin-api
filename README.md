### weixin-api
weixin api for miniprogram and minigame.
```
pip install -U weixin-api
```

### Usage
```
import weixin_api

weixin_api.auth: 登录
weixin_api.media: 素材
weixin_api.message: 客服消息
weixin_api.qrcode: 二维码
weixin_api.template: 模板消息
weixin_api.sns: sns相关
```

pay:
```
from weixin_api.midas import MidasPay

midas_pay = MidasPay(
    app_id='appid',
    offer_id='12345678',
    app_key='app_key',
    sandbox=False,
)

midas_pay.getbalance(access_token, session_key, open_id, **kwargs)
midas_pay.pay(access_token, session_key, open_id, bill_no, amount, **kwargs)
midas_pay.cancelpay(access_token, session_key, open_id, bill_no, **kwargs)
midas_pay.present(access_token, session_key, open_id, bill_no, **kwargs)
```