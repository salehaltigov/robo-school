# Generated by Django 3.2.16 on 2023-09-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0003_trainer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]
