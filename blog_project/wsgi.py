import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path  # ✅ Necesario para BASE_DIR

BASE_DIR = Path(__file__).resolve().parent.parent  # ✅ Define BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'media'), prefix='media/')
