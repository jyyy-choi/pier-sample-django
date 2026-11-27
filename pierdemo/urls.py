import platform

import django
from django.http import HttpResponse, JsonResponse


def index(_request):
    import psycopg2

    return HttpResponse(
        f"""<!doctype html><meta charset="utf-8"><title>pier sample · django</title>
<main style="font-family:system-ui;margin:3rem auto;max-width:34rem;line-height:1.7">
<h1>pier sample · Django (gunicorn)</h1>
<p>Django {django.get_version()} · Python {platform.python_version()} · psycopg2 {psycopg2.__version__.split()[0]}</p>
<p>psycopg2 는 wheel 이 없어 빌드 이미지에서 컴파일되고, 실행 이미지의 libpq5 로 적재됩니다.</p>
<p><a href="/healthz">/healthz</a></p></main>"""
    )


def healthz(_request):
    return JsonResponse({"ok": True, "django": django.get_version()})


from django.urls import path  # noqa: E402

urlpatterns = [path("", index), path("healthz", healthz)]
