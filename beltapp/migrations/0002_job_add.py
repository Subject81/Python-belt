# Generated by Django 2.2 on 2020-01-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='add',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
