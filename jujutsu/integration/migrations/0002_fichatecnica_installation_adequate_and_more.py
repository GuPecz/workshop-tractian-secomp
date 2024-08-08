# Generated by Django 5.1 on 2024-08-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichatecnica',
            name='installation_adequate',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='fichatecnica',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
