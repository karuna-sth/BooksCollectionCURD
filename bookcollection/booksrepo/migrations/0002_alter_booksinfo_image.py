# Generated by Django 4.2 on 2023-04-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksrepo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksinfo',
            name='image',
            field=models.ImageField(upload_to='static/bookImage'),
        ),
    ]
