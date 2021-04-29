from pathlib import Path
from decouple import config
import django_heroku
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm)g&gv*5iw*eq0fi48=5nv#hjn$eey^ujpyx_6y^u2ryfbtebnk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'schoolmarks.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'sendmail.apps.SendmailConfig',
    'directory_page.apps.DirectoryPageConfig',
    'semester_dates.apps.SemesterDatesConfig',
    'enter.apps.EnterConfig',
    'reports.apps.ReportsConfig',
    'users.apps.UsersConfig',
    'main.apps.MainConfig', 
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hitcount',
    'bootstrap_datepicker_plus',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Marks.urls'

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

WSGI_APPLICATION = 'Marks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'marksdb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env) 

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'#'en-gb'

#DATE_INPUT_FORMATS = ['%d-%m-%Y', '%Y-%m-%d']

#DATE_FORMAT = "%d-%m-%Y"

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    #'/var/www/static/',
]

#STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
#'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEBUG_PROPAGATE_EXCEPTIONS = True
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# Email settings
EMAIL_HOST = 'smtp.gmail.com' #'localhost'
EMAIL_HOST_USER =  config('email_host_user',default='') #''
EMAIL_HOST_PASSWORD = config('email_host_password',default='') #'' 
EMAIL_PORT = 587 #'1025' 
EMAIL_USE_TLS = True #False

                                          #console  
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

django_heroku.settings(locals())