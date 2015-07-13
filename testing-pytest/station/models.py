from django.db import models


class Station(models.Model):
    call_sign = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.call_sign

    def is_weta(self):
        return self.call_sign == 'weta'

    def is_koth(self):
        return self.call_sign == 'koth'
