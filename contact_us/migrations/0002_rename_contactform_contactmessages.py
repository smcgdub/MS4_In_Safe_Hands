# Generated by Django 3.2.7 on 2021-10-06 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='ContactMessages',
        ),
    ]
