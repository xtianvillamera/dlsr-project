# Generated by Django 2.1.7 on 2019-04-05 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkcard', '0008_auto_20190405_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_no',
            field=models.IntegerField(),
        ),
    ]