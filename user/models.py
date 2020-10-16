from django.db import models


class User(models.Model):
    '''user 表的数据模型'''
    GENDERS = (
        ('male', '男性'),
        ('female', '女性'),
    )
    LOCATION = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ('武汉', '武汉'),
        ('沈阳', '沈阳'),
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    gender = models.CharField(max_length=10, default='male', choices=GENDERS, verbose_name='性别')
    birthday = models.DateField(default='1990-01-01', verbose_name='生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=20, default='北京', choices=LOCATION, verbose_name='常居地')

    vip_id = models.IntegerField(default=1, verbose_name='用户对应的会员ID')
    vip_end = models.DateTimeField(default='2100-01-01', verbose_name='会员过期时间')

    def __str__(self):
        return str(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.gender,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }


class Profile(models.Model):
    '''个人的配置及交友资料'''
    dating_gender = models.CharField(max_length=10, default='male', choices=User.GENDERS,
                                     verbose_name='匹配的性别')
    dating_location = models.CharField(max_length=20, default='北京', choices=User.LOCATION,
                                   verbose_name='⽬标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最⼩查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最⼤查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最⼩交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最⼤交友年龄')
    vibration = models.BooleanField(verbose_name='开启震动')
    only_matched = models.BooleanField(verbose_name='不让为匹配的⼈看我的相册')
    auto_play = models.BooleanField(verbose_name='⾃动播放视频')

    def to_dict(self):
        return {
            'id': self.id,
            'dating_gender': self.dating_gender,
            'dating_location': self.dating_location,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'vibration': self.vibration,
            'only_matched': self.only_matched,
            'auto_play': self.auto_play,

        }