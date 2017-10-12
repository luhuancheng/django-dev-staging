### django开发脚手架

### 项目目录结构
```
deploy_server/
├── deploy_server
│   ├── apps
│   │   ├── __init__.py
│   │   └── user
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── __init__.py
│   │       ├── migrations
│   │       │   └── __init__.py
│   │       ├── models.py
│   │       ├── tests.py
│   │       └── views.py
│   ├── __init__.py
│   ├── libs
│   │   └── __init__.py
│   ├── settings
│   │   ├── common.py
│   │   ├── dev.py
│   │   ├── __init__.py
│   │   └── prod.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
├── requirements
│   ├── common.txt
│   ├── dev.txt
│   └── prod.txt
└── requirements.txt
```

### 额外说明
###### 由于更改了项目目录结构，需要修改配置settings/common.py，加入以下内容
```
# 设置apps加载路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'libs'))
```

###### 使用vue作为前端框架，需要修改配置settings/common.py, 将静态资源路径指向vue打包后的路径
```
# 设置静态文件路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/dist/static'),
]
```
###### 使用vue作为前端框架，需要修改配置settings/common.py, 将模版加载路径指向vue打包后的路径
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 修改模版加载路径
        'DIRS': [os.path.join(BASE_DIR, 'frontend/dist')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 编码规范
###### 包的导入顺序
```
# 标准库
from math import sqrt
from os.path import abspath

# Django核心库
from django.db import models
from django.utils.translation \
    import ugettext_lazy as _

# 第三方应用
from django_extensions.db.models \
    import TimeStampedModel

# local应用
from splits.models import BananaSplit
```

###### 使用相对路径导入
```
from .models import Report
from .forms import ReportForm
```

### 打包前端文件
```
cd frontend
# 安装相关开发包
npm install

# 打包, 将在当前目录生成一个dist目录放置打包后的文件
npm run build
```

### 启动开发服务器
```
shell> cd deploy_server
# 使用开发环境配置
shell> export RUNNING=DEV
# 使用正式环境配置
shell> export RUNNING=PROD
# 启动
shell> python manager.py runserver 0:8080
```
