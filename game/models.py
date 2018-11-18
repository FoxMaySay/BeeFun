# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.db import models
from django.urls import reverse
from simditor.fields import RichTextField


# 游戏详情
class GameDetail(models.Model):
    game_id = models.AutoField(primary_key=True)
    zh_name = models.CharField(max_length=20)
    en_name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='icon/%Y/%m')
    star = models.IntegerField(choices=((1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')), default=3)
    website = models.URLField(blank=True, null=True)
    platform = models.CharField(max_length=15)
    tags = models.CharField(max_length=15)
    contract_address = models.URLField(blank=True, null=True)
    short_description = models.CharField(max_length=30)
    parti_description = RichTextField()
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Game Detail'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zh_name


# 页面统计
class GameView(models.Model):
    zh_name = models.ForeignKey(GameDetail, on_delete=models.CASCADE)
    view_number = models.PositiveIntegerField(default=0)
    like_number = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Web Analytics'
        verbose_name_plural = verbose_name


# 社交平台
class GameSocial(models.Model):
    zh_name = models.ForeignKey(GameDetail, on_delete=models.CASCADE)
    contact_wechat = models.CharField(max_length=20, blank=True, null=True)
    contact_qq = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(max_length=30, blank=True, null=True)
    official_wechat = models.CharField(max_length=20, blank=True, null=True)
    official_weibo = models.URLField(blank=True, null=True)
    official_facebook = models.URLField(blank=True, null=True)
    official_twitter = models.URLField(blank=True, null=True)
    official_telegram = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Sccial Contact'
        verbose_name_plural = verbose_name


# 反馈信息
class Feedback(models.Model):
    feedback = models.CharField(max_length=300)
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = verbose_name


# 首页Banner
class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner/%Y/%m')
    url = models.URLField()
    index = models.IntegerField(default=100)
    is_show = models.IntegerField(choices=((1, '显示'), (0, '不显示')), default=0)
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = verbose_name


# 友情连接
class Blogroll(models.Model):
    website_name = models.CharField(max_length=15)
    website_link = models.URLField()
    remark = models.CharField(blank=True, null=True, max_length=30)

    class Meta:
        verbose_name = 'Blogroll'
        verbose_name_plural = verbose_name
