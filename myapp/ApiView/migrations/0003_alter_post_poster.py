# Generated by Django 5.1.4 on 2024-12-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiView', '0002_alter_post_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
