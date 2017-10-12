# coding=utf-8
import os

from .common import *


# 开发环境: DEV
# 正式环境: PROD
env = os.getenv('RUNNING', 'DEV')
print("You are running on {}".format(env))
if env == 'PROD':
    from .prod import *
else:
    from .dev import *
