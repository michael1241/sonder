# Generated by Django 2.2 on 2019-04-14 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysissource',
            name='stockfish_version',
        ),
        migrations.AddField(
            model_name='gameanalysis',
            name='stockfish_version',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]
