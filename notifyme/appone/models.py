from django.db import models

# Create your models here.
class Clgsdb(models.Model):
    clg_id = models.AutoField(primary_key=True)
    clg_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clgsdb'


class Clgtagsdb(models.Model):
    clgtag_id = models.AutoField(primary_key=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clgtagsdb'


class Detailsdb(models.Model):
    student_id = models.AutoField(primary_key=True)
    clg_id = models.IntegerField(blank=True, null=True)
    student_type = models.CharField(max_length=100, blank=True, null=True)
    student_name = models.CharField(max_length=100, blank=True, null=True)
    student_email = models.CharField(max_length=200, blank=True, null=True)
    student_password = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailsdb'


class Eventsdb(models.Model):
    event_id = models.AutoField(primary_key=True)
    clg_id = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    event_name = models.CharField(max_length=100, blank=True, null=True)
    event_desc = models.CharField(max_length=200, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    event_photourl = models.CharField(max_length=200, blank=True, null=True)
    event_attenders = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventsdb'

class Tagsdb(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tagsdb'
