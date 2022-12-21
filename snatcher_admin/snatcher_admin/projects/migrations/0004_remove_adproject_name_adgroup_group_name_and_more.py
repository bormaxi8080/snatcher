# Generated by Django 4.1.4 on 2022-12-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_ad_created_at_alter_ad_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adproject',
            name='name',
        ),
        migrations.AddField(
            model_name='adgroup',
            name='group_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='adproject',
            name='project_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]