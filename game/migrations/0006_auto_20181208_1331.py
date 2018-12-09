# Generated by Django 2.1.3 on 2018-12-08 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20181207_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedetail',
            name='show_name',
            field=models.CharField(default='cat', max_length=20),
        ),
        migrations.AlterField(
            model_name='gamedetail',
            name='en_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gamedetail',
            name='zh_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
