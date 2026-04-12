import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username=os.environ["DJANGO_SUPERUSER_USERNAME"]).exists():
    User.objects.create_superuser(
        username=os.environ["DJANGO_SUPERUSER_USERNAME"],
        email=os.environ["DJANGO_SUPERUSER_EMAIL"],
        password=os.environ["DJANGO_SUPERUSER_PASSWORD"]
    )