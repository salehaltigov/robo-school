# Generated by Django 3.2.16 on 2023-09-15 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Наименование')),
                ('icon', models.CharField(blank=True, help_text='Необходим класс mdi', max_length=50, null=True, verbose_name='Иконка')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на социальную сеть')),
            ],
            options={
                'verbose_name': 'Социальная сеть пользователя',
                'verbose_name_plural': 'Социальные сети пользователя',
            },
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='link',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='sociallinkname',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='social',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer', verbose_name='Пользователь'),
        ),
    ]
