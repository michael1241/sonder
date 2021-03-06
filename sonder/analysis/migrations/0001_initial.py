# Generated by Django 2.2 on 2019-04-14 03:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import sonder.analysis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('secret_token', models.CharField(default=sonder.analysis.models.create_api_token, max_length=12, unique=True)),
                ('stockfish_version', models.CharField(max_length=8)),
                ('use_for_irwin', models.BooleanField(default=False)),
                ('use_for_mods', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lichess_id', models.CharField(max_length=32, unique=True)),
                ('time_control', models.CharField(max_length=8)),
                ('is_analyzed', models.BooleanField(default=False)),
                ('moves', django.contrib.postgres.fields.jsonb.JSONField()),
                ('moves_emt', django.contrib.postgres.fields.jsonb.JSONField()),
                ('moves_blur', django.contrib.postgres.fields.jsonb.JSONField()),
                ('moves_masterdb_matches', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='IrwinReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('origin', models.CharField(max_length=32)),
                ('owner', models.CharField(blank=True, max_length=255)),
                ('precedence', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IrwinReportRequiredGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.Game')),
                ('irwin_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.IrwinReport')),
            ],
        ),
        migrations.AddField(
            model_name='irwinreport',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='black_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games_as_black', to='analysis.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='white_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games_as_white', to='analysis.Player'),
        ),
        migrations.CreateModel(
            name='GameAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis', django.contrib.postgres.fields.jsonb.JSONField()),
                ('nodes', models.IntegerField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Game')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.AnalysisSource')),
            ],
            options={
                'index_together': {('game', 'source')},
            },
        ),
    ]
