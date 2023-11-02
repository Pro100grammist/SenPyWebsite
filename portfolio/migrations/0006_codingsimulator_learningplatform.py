# Generated by Django 4.2.2 on 2023-11-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_frontend_gitservices_paas'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingSimulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/dropmenu/cs/')),
                ('url', models.URLField()),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LearningPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/dropmenu/platform/')),
                ('url', models.URLField()),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
