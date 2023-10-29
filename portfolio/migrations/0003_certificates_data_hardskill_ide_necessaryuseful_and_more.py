# Generated by Django 4.2.2 on 2023-10-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_projects_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='portfolio/about/')),
                ('alt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/dropmenu/data/')),
                ('url', models.URLField()),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url_name', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='IDE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/dropmenu/ides/')),
                ('url', models.URLField()),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NecessaryUseful',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url_name', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WebFrameworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/dropmenu/web/')),
                ('url', models.URLField()),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]