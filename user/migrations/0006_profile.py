# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-15 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200814_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_gender', models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=10, verbose_name='匹配的性别')),
                ('dation_location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('成都', '成都'), ('西安', '西安'), ('武汉', '武汉'), ('沈阳', '沈阳')], default='北京', max_length=20, verbose_name='⽬标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最⼩查找范围')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最⼤查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最⼩交友年龄')),
                ('max_dating_age', models.IntegerField(default=50, verbose_name='最⼤交友年龄')),
                ('vibration', models.BooleanField(verbose_name='开启震动')),
                ('only_matche', models.BooleanField(verbose_name='不让为匹配的⼈看我的相册')),
                ('auto_play', models.BooleanField(verbose_name='⾃动播放视频')),
            ],
        ),
    ]
