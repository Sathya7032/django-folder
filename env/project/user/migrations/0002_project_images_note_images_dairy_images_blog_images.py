# Generated by Django 4.2.5 on 2023-10-03 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='Photos')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Note_Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='Photos')),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.notes')),
            ],
        ),
        migrations.CreateModel(
            name='Dairy_Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='Photos')),
                ('dairy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.dairy')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='Photos')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.blogs')),
            ],
        ),
    ]
