# Generated by Django 3.2.7 on 2024-11-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_shared', '0004_video_formation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link_chromedriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_url', models.CharField(blank=True, max_length=500, null=True)),
                ('download_path_chromedriver', models.CharField(blank=True, max_length=1500, null=True)),
            ],
        ),
    ]
