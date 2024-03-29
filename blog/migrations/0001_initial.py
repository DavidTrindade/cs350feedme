# Generated by Django 3.1.3 on 2021-02-12 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_link', models.CharField(max_length=2000)),
                ('link', models.CharField(max_length=2000)),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('favourite', models.ManyToManyField(blank=True, related_name='feeds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=2000)),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.feed')),
            ],
        ),
    ]
