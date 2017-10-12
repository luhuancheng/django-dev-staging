# coding=utf-8
# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'deploy_server',
        'USER': 'root',
        'PASSWORD': 'P#ssw0rd',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'ATOMIC_REQUEST': True
    }
}
