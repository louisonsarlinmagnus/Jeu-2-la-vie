# Generated by Django 4.0.4 on 2022-04-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, verbose_name='Nom de la forme')),
                ('description', models.CharField(max_length=200, verbose_name='Description de la forme')),
                ('cellules', models.TextField(verbose_name='Cellules qui composent la forme')),
            ],
        ),
    ]