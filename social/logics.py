import datetime

from user.models import User
from user.models import Profile


def rcmd():
    '''通过数据库推荐用户'''
    # 获取当前用户的交友资料

    profile, _ = Profile.objects.get_or_create(id=uid)

    # 计算出生日期的范围
    today = datetime.date.today()
    earliest_birthday = today - datetime.timedelta(profile.max_dating_age * 365)  # 最早出生日期
    latest_birthday = today - datetime.timedelta(profile.min_dating_age * 365)  # 最晚出生日期

    # 根据条件匹配要推荐的用户
    User.objects.filter(
        gender=profile.dating_gender,
        location=profile.dating_location,
        birthday__gte=earliest_birthday,
        birthday__lte=latest_birthday
      )[:30]


