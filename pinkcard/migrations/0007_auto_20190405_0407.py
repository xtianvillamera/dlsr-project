# Generated by Django 2.1.7 on 2019-04-05 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinkcard', '0006_auto_20190405_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree_prog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pinkcard.DegreeProg'),
        ),
    ]
