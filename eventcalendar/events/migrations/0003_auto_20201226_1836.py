# Generated by Django 3.1.3 on 2020-12-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201226_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='user',
        ),
        migrations.AddField(
            model_name='participant',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]