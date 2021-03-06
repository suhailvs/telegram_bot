# Generated by Django 3.1.5 on 2021-01-26 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(null=True)),
                ('username', models.CharField(default='', max_length=200)),
                ('firstname', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CallCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegrambot.telegramuser')),
            ],
        ),
    ]
