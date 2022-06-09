from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from .choices import MODE_CHOICES

# Create your models here.

class Draft(models.Model):
    
    class Meta:
        verbose_name = ('禁选')
        verbose_name_plural = ('禁选')

    mode = models.CharField(
        verbose_name="模式", max_length=20, choices=MODE_CHOICES, default='1'
    )

    match_name = models.CharField(
        verbose_name='匹配名称', max_length=255
    )

    code = models.CharField(
        verbose_name='房间 编号', unique=True, null=True, max_length=255
    )

    password = models.CharField(
        verbose_name='密码', max_length=255
    )

    blue_team_name = models.CharField(
        verbose_name='蓝队名称', max_length=255
    )

    blue_player_name = models.CharField(
        verbose_name='蓝队队员姓名', default='', max_length=100
    )

    red_team_name = models.CharField(
        verbose_name='红队名称', max_length=255
    )

    red_player_name = models.CharField(
        verbose_name='红队队员姓名', default='', max_length=100
    )

    banpick = models.CharField(
        verbose_name='禁选Data', max_length=255, blank=True
    )

    banpick_final = models.CharField(
        verbose_name='禁选结果', max_length=255, blank=True, default=""
    )

    blue_done = models.BooleanField(
        verbose_name='蓝队选择', default=False
    )

    red_done = models.BooleanField(
        verbose_name='红队选择', default=False
    )

    timer = models.DateTimeField(
        verbose_name="开始", blank=True, null=True
    )

    date = models.DateTimeField(
        verbose_name="暂停", default=timezone.now
    )
    
    def __str__(self):
        return f'{self.match_name}'

    def entry_url(self):
        return f'/draft/entry/{self.code}'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

class Champion(models.Model):

    class Meta:
        verbose_name = ('角色')
        verbose_name_plural = ('角色')

    no = models.CharField(verbose_name='角色编号', max_length=3, default='')
    name = models.CharField(verbose_name='角色姓名', max_length=20, default='', help_text='请输入名字。 例）可莉')
    lane = models.CharField(verbose_name='位置', max_length=20, default='', help_text='请输入名字。 例）可莉')
    keyword = models.CharField(verbose_name="关键词", max_length=20, default="")

    def __str__(self):
        return f'{self.name}'