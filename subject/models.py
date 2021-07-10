from django.db import models
from eSchoolGateProject import settings


class Subject(models.Model):
    name = models.CharField(max_length=100,)
    teacher = models.ManyToManyField(settings.AUTH_USER_MODEL)
    classroom = models.CharField(max_length=7,)

    def __unicode__(self):
        return self.name + ' - ' + self.classroom


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, related_name='lesson', on_delete=models.CASCADE)
    topic = models.CharField(default='', max_length=500)
    description = models.CharField(default='', max_length=500)
    week = models.IntegerField(unique=True)
    video = models.FileField(upload_to='media/videos')
    note = models.FileField(upload_to='media/notes')

