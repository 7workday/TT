'''各种缓存的key'''

VCODE_K = 'Vcode-%s'  #验证码的key,拼接用户手机号
FIRST_RCMD_K = 'FIRST_RCMD_K-%s'  #优先推荐队列,拼接用户id
REWIND_K = 'Rewind-%s-%s'  # 记录每日反悔次数的 Key，拼接当天的日期和uid
MODEL_K = 'Model-%s-%s'  # 缓存每一个 Model 的 Key, 拼接 Model 的名字 和 对应的 model 实例的 id
RANK_K = 'HotRank'