# Generated by Django 4.2.6 on 2023-10-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0001_initial'),
        ('accounts', '0005_alter_userprofile_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='categories',
            field=models.ManyToManyField(blank=True, to='handbook.category', verbose_name='Категории'),
        ),
    ]
