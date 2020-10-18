'''程序配置,及第三方平台配置'''



SWIPE_SCORE = {
    'like': 5,
    'superlike': 7,
    'dislike': -5,
}


# Redis配置
REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 6,
}

YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_ARGS = {
    "sid": "52a8458e04af4682305c20ffaa41facf",
    "token": "4bee9c80815aa77bebf5bf2b64695a17",
    "appid": "e1a22b6fcc23437f98e00709cc94a1fc",
    "templateid": "527013",
    "param": None,
    "mobile": None,
}

# YZX_SID: "52a8458e04af4682305c20ffaa41facf"  #用户的账号唯一标识“Account Sid”，在开发者控制台获取
# YZX_TOKEN: "4bee9c80815aa77bebf5bf2b64695a17"  #用户密钥，在开发者控制台获取
# YZX_APPID: "e1a22b6fcc23437f98e00709cc94a1fc"  #创建应用时系统分配的唯一标示
# YZX_TEMPLATEID: "527013"  #创建短信模板时系统分配的唯一标示
# YZX_PARAM: None  #模板中的替换参数
# YZX_MOBILE: None  #接收的单个手机号



# 七牛云配置
QN_ACCESSKEY = "DYSuwOi8md-nze_HpzGHrasygQpeUbSb5Vezp_oO"
QN_SECRETKEY = "2aks2grACSSXmQjCWu9HyIXlR-Myrs_oEDxsdFGb"
QN_BUCKET = 'sh1906'
QN_BASE_URL = 'http://qgqtuv53f.hd-bkt.clouddn.com'