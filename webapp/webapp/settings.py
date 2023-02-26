"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

#用来绑定当前项目的绝对路径（动态计算出来的），多有文件夹都可以依赖此路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('结果是'+str(os.path.abspath(__file__)))
print('结果是'+str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z2_por6=l$a6($&sx66n)+tcw9#_i4fc9%thpuwcr^0dg@@igp'

# SECURITY WARNING: don't run with debug turned on in production!
#调试模式
#TRUE -调试模式
#1,检测代码改动后，立刻重启服务
#2，报错页面
#FALSE -正式启动模式/上线模式；
DEBUG =True  #将debug关闭后即可以显示标准404页面 正式上线要关闭debug

#请求头host头，过滤掉一些值，但是debug的时候默认接受locahost和127.0.0.1的值
#设置允许访问到本项目的host值
#所以测试的时候也可以不用配置（可以为空）
#上线可以把网站的域名写进来，不是来源于本网站域名的请求坚决不让进
ALLOWED_HOSTS = []


# Application definition
#web中间件，指定当前项目中安装的应用列表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#用于注册中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#用于主url配置
ROOT_URLCONF = 'webapp.urls'


#用于指定模板的配置信息
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#用于指定数据库的配置信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_bbs',
        'USER':'work',
        'PASSWORD':'djangobbs',
        'HOST':'127.0.0.1',
        'port':'3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


#语言设置 'zh-Hans'设置为中文
LANGUAGE_CODE = 'zh-Hans'

#时区 默认是'UTC'格林威治时间 ''
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'