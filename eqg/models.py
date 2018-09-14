from django.db.models import CharField, Model

class Datasets(Model):
    name = CharField(max_length=200)


