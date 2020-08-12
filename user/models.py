from django.db import models

# Create your models here.
class User(models.Model):
    GENDERS = (
        ('male','男性'),
        ('female','女性'),
    )

    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('武汉', '武汉'),
        ('成都', '成都'),
        ('西安', '西安'),
        ('沈阳', '沈阳'),
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=20, db_index=True, verbose_name='昵称')
    gender = models.CharField(max_length=10, choices=GENDERS, default='male', verbose_name='性别')
    birthday = models.DateField(default='2000-01-01', verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象 URL')
    location = models.CharField(max_length=10, default='上海', choices=LOCATIONS, verbose_name='常居地')