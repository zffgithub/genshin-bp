from .base import *
from banpick.utils import get_server_info_value

SETTINGS_PROD_DIC = {} # get_server_info_value("production")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "123" # SETTINGS_PROD_DIC["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': SETTINGS_PROD_DIC['DATABASES']['default']
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认
        'NAME': 'genshin-im',  # 连接的数据库
        'HOST': '192.168.0.130',  # mysql的ip地址
        'PORT': 3306,  # mysql的端口
        'USER': 'root',  # mysql的用户名
        'PASSWORD': 'root'  # mysql的密码
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('192.168.0.130', 6379)],
        },
    }
}