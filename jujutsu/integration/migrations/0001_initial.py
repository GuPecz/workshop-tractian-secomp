# Generated by Django 5.1 on 2024-08-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FichaTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('fabricante', models.CharField(max_length=100)),
                ('img1', models.ImageField(null=True, upload_to='media/')),
                ('img2', models.ImageField(null=True, upload_to='media/')),
                ('img3', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
    ]
