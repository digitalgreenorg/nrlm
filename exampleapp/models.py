from django.db import models

# Create your models here.

class State(models.Model):
    name=models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Persons(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    city=models.CharField(max_length=20)
    state=models.ForeignKey(State)
    def __unicode__(self):
        return "%s, %s" % (self.name,self.city)
    def save(self, *args, **kwargs):
        # For automatic slug generation.

        return super(Persons, self).save(*args, **kwargs)