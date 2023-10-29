# Generated by Django 4.2.2 on 2023-10-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_certificates_data_hardskill_ide_necessaryuseful_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebServers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/dropmenu/server/')),
                ('url', models.URLField()),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
