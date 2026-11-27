import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "pier-sample-not-a-real-secret")
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
# pier 가 붙여 주는 자동 주소로 들어오므로 호스트를 제한하지 않는다 (샘플)
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["https://*.picksell.io"]

INSTALLED_APPS = ["django.contrib.staticfiles"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "pierdemo.urls"
TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True, "DIRS": []}]
WSGI_APPLICATION = "pierdemo.wsgi.application"

# 실제로 접속하지는 않는다 (psycopg2 가 설치·적재되는지 확인용)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "pier"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
USE_TZ = True
TIME_ZONE = "Asia/Seoul"
