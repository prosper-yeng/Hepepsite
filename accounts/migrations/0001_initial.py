# Generated by Django 3.0.5 on 2020-04-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HepepsTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pics')),
                ('Desc', models.TextField()),
                ('Read_more', models.CharField(max_length=200)),
            ],
        ),
    ]