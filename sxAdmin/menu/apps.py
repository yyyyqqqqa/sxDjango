import os


from django.apps import AppConfig

app_name = os.path.basename(os.path.dirname(__file__))

class MenuConfig(AppConfig):
    name = app_name
