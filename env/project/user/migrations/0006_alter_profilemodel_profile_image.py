# Generated by Django 4.2.5 on 2023-10-07 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profilemodel_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(upload_to='Photos'),
        ),
    ]