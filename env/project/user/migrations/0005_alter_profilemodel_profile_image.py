# Generated by Django 4.2.5 on 2023-10-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_profile_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='Photos'),
        ),
    ]
