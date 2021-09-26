import datetime

from django.db import models

class Employee(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20)
    card_id = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE,
                             related_name='user_attendance')
    date = models.DateField(default=datetime.datetime.now())
    log_in = models.TimeField(default=datetime.datetime.now())
    log_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.user.name



