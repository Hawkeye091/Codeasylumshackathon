# Generated by Django 2.2.3 on 2019-07-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clgsdb',
            fields=[
                ('clg_id', models.AutoField(primary_key=True, serialize=False)),
                ('clg_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'clgsdb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clgtagsdb',
            fields=[
                ('clgtag_id', models.AutoField(primary_key=True, serialize=False)),
                ('clg_id', models.IntegerField(blank=True, null=True)),
                ('tag_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clgtagsdb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detailsdb',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('clg_id', models.IntegerField(blank=True, null=True)),
                ('student_type', models.CharField(blank=True, max_length=100, null=True)),
                ('student_name', models.CharField(blank=True, max_length=100, null=True)),
                ('student_email', models.CharField(blank=True, max_length=200, null=True)),
                ('student_password', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'detailsdb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventsdb',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('clg_id', models.IntegerField(blank=True, null=True)),
                ('tag_id', models.IntegerField(blank=True, null=True)),
                ('event_name', models.CharField(blank=True, max_length=100, null=True)),
                ('event_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_photourl', models.CharField(blank=True, max_length=200, null=True)),
                ('event_attenders', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'eventsdb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Followsdb',
            fields=[
                ('follow_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.IntegerField(blank=True, null=True)),
                ('tag_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'followsdb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tagsdb',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tagsdb',
                'managed': False,
            },
        ),
    ]
