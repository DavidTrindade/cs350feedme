# Generated by Django 3.1.3 on 2021-02-23 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]