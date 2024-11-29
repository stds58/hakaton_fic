from .celery import app as celery_app

# Это необходимо для того, чтобы Celery работал в Django
# при запуске Django использовать: python -m celery -A your_project_name worker

__all__ = ['celery_app']
