# Generated by Django 2.1.4 on 2019-02-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elecric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lol', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('dept_inst', models.CharField(max_length=50)),
                ('student_no', models.IntegerField()),
                ('rem_hours', models.DurationField()),
            ],
        ),
    ]