# Generated by Django 2.1.4 on 2019-03-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewing', '0003_auto_20190308_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='password', max_length=30),
        ),
    ]