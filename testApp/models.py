from django.db import models

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=100, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    saddress = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.sname
    
    class Meta:
        managed = False
        db_table = 'student'
