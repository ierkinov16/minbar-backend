# Generated by Django 4.2.3 on 2023-07-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clerics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=400)),
                ('profile_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
