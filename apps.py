from django.apps import AppConfig


class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Homepage'


class bauwongconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bauwong'


class suche_namenconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Zahlen'


class loesche_datenconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bezahlen'
