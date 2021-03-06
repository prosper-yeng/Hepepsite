# Generated by Django 3.0.5 on 2020-05-09 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200503_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_desc', models.TextField()),
                ('post_img', models.ImageField(upload_to='pics')),
                ('img_title', models.CharField(max_length=200)),
                ('post_category', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('post_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.HepepsTeam', verbose_name='Post By')),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
