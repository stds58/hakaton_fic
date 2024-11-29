from celery import shared_task
import requests


@shared_task
def start_help_filling():
    # host 127.0.0.1 not docker compose or module_image:8001 with docker compose
    r = requests.get("http://127.0.0.1:8000/") # тут пишем ручку api
    #
    if r.status_code == 200:
        return "Запуск состоялся"
        # return r.json()

