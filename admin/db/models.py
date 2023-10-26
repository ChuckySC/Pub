from django.db import models

class BaseTimestampModel(models.Model):
    rid = models.DateTimeField(db_column='rid', auto_now_add=True)
    rud = models.DateTimeField(db_column='rud', auto_now=True)

    class Meta:
        abstract = True