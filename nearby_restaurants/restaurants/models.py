from django.db import models

class Restaurants(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    vicinity = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurants'
