# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# ضبط الإعدادات الافتراضية لدجانجو
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')

# استخدام الإعدادات المكونة في ملف settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# اكتشاف المهام تلقائيًا من تطبيقات دجانجو
app.autodiscover_tasks()
