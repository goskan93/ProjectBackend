# Generated by Django 2.2.6 on 2019-11-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Countries',
            field=models.ManyToManyField(to='blogs.Country'),
        ),
        migrations.AddField(
            model_name='blog',
            name='Languages',
            field=models.ManyToManyField(to='blogs.Language'),
        ),
    ]
